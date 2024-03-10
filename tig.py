import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import random
import streamlit as st
import time


st.set_page_config(
    page_title="tig",
    page_icon="📜",
)


def calculate_font_size(draw, sentence, font_path, image_width, image_height, max_font_size=100):
    font_size = max_font_size

    while True:
        font = ImageFont.truetype(font_path, font_size)
        text_width, text_height = draw.textbbox(xy=(0,0),text=sentence, font=font)[2:4]

        if text_width < image_width and text_height < image_height:
            break

        font_size -= 1
        if font_size <= 0:
            break

    return font_size

def generate_images(df, output_folder, image_width=200, image_height=64, num_images=None):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    data_list = []

    progress_bar = st.progress(0)
    status_text = st.empty()
    start_time = time.time()

    for index, row in enumerate(df.head(num_images).iterrows(), start=1):
        sentence = row[1].iloc[0]

        font_dir = './font_files'
        font_files = os.listdir(font_dir)
        font_files = [f for f in font_files if f.endswith(('ttf', 'otf', 'woff', 'woff2', 'eot', 'pfb'))]
        picked_font = random.choice(font_files)
        font_path= os.path.join(font_dir , picked_font)

        img = Image.new('RGB', (image_width, image_height), color='white')
        draw = ImageDraw.Draw(img)

        font_size = calculate_font_size(draw, sentence, font_path, image_width, image_height)

        font = ImageFont.truetype(font_path, font_size)

        text_width, text_height = draw.textbbox(xy=(0,0),text=sentence, font=font)[2:4]

        x = (image_width - text_width) // 2
        y = (image_height - text_height) // 2

        draw.text((x, y), sentence, font=font, fill='black')

        word_count = len(sentence.split())

        img_name = f"{index}.png"
        img_path = os.path.join(output_folder, img_name)
        img.save(img_path)

        data_list.append({'image_file': img_name, 'text': sentence, 'font_size': font_size, 'font_file': picked_font, 'word_count': word_count})

        elapsed_time = time.time() - start_time
        iterations_per_second = index / elapsed_time
        time_remaining = (num_images - index) / iterations_per_second

        progress_bar.progress(index / num_images)
        status_text.text(f'Processed: {index}/{num_images}, Elapsed: {elapsed_time:.2f}s, Remaining: {time_remaining:.2f}s, Speed: {iterations_per_second:.2f} iterations/s')

    csv_path = os.path.join("./", 'data.csv')
    data_df = pd.DataFrame(data_list)
    data_df.to_csv(csv_path, index=False)

    st.write(f"{num_images} images and data for the first {num_images} rows saved successfully in {output_folder}")

def main():
    st.title("Text to Image Generator")

    file = st.file_uploader("Upload a file", type=['csv', 'xlsx', 'txt'])
    image_width = st.number_input("Enter Image Width", value=900)
    image_height = st.number_input("Enter Image Height", value=64)
    num_images = st.number_input("Enter Number of Images", value=10)

    if st.button("Generate Images"):
        if file is not None:
            if file.type == 'text/csv':
                df = pd.read_csv(file, encoding='utf-8')
            elif file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                df = pd.read_excel(file, encoding='utf-8')
            elif file.type == 'text/plain':
                df = pd.read_csv(file, sep="\t", encoding='utf-8')
            generate_images(df, 'output_images', image_width, image_height, num_images)
        else:
            st.write("Please upload a file.")

if __name__ == "__main__":
    main()