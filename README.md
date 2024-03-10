
# Text to Image Generator

A synthetic text image pair generator for OCR

## Installation

install the required dependencies first

```bash
pip install -r requirements.txt
```

Launch the web app interface
```bash
streamlit run tig.py
```

It will automatically launch the instance on the browser, if not click on the local URL in terminal

![local_url](https://github.com/prathameshza/TextToImageGenerator/assets/46810093/66ce3475-915c-4e63-b8a0-e731b79bbb3f)

Below interface will pop up!

![tig_interface](https://github.com/prathameshza/TextToImageGenerator/assets/46810093/6bd0c568-ef86-4cb9-8491-8b4a9de8a7b1)

## How to use

Upload the Text/CSV/Excel file containing sentences or words,
Below is a sample of text file containing words

![SampleWords](https://github.com/prathameshza/TextToImageGenerator/assets/46810093/77aec91e-9a2b-4505-99ad-89a88af48dc6)


Set the image width, image height (in pixels) and the number of image to be generated

The generated images will be stored in the **output_images** directory and a **data.csv** file containing the image name, text, font size, font file and word count as shown Below

![datacsv](https://github.com/prathameshza/TextToImageGenerator/assets/46810093/b70b189d-625d-45b6-a62b-ec5cc2b5119f)

## Generated Samples

#### words:

![1](https://github.com/prathameshza/TextToImageGenerator/assets/46810093/32defbb9-7ce6-4fda-95f9-408b63225fab)
![2](https://github.com/prathameshza/TextToImageGenerator/assets/46810093/0dda3734-f2e3-47ff-b99f-d1467022cbb0)

#### sentences:

![4](https://github.com/prathameshza/TextToImageGenerator/assets/46810093/9525d8fe-9ca8-4ba3-a63f-6c4aaf08565f)
![3](https://github.com/prathameshza/TextToImageGenerator/assets/46810093/2dcc2a87-8547-472f-aac2-1c5a305a55bb)

## Language support

All languages are supported 🥳 just use the proper font files.


## Customization
The app will choose the fonts randomly, if you want to use only a single specific font then download and paste it into the **font_files** directory

supported font formats include: ttf, otf, woff, woff2, eot and pfb

> Note: Changing the font also changes the images created per second
#### Below is the tested font and their speeds for Hindi image generation
| Font            | Speed     |
|----------------:|-----------|
|Lohit-Devanagari | 15-16 it/s|
|Gargi            | 17-18 it/s|
|Sura unicode     | 11-12 it/s|
|akshra unicode   | 4-5 it/s  |
|Kurti dev 010    | 50-55 it/s|
|aakar regular    | 50-55 it/s|
|freesansbold     | 9-10 it/s |
|Nakula           | 8-9 it/s  |
