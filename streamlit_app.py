import os
os.system('pip install paddlepaddle')
os.system('pip install paddleocr')
import numpy as np
from PIL import Image
import streamlit as st
import tensorflow as tf
from helper import get_model
from paddleocr import draw_ocr

st.markdown("<h1 style='text-align: center; color: black;'>OCR</h1>", unsafe_allow_html=True)

def select_language():
    option = st.selectbox(
        'Choose language',
        ('Arabic', 'Welsh', 'Hindi', 'Nepali', 'Spanish', 'Tamil', \
        'English', 'Chinese', 'Korean', 'Japan', 'French', \
        'German', 'Italian'))
    return option

def select_image():
    image = st.file_uploader("Upload your image here", type=['jpg','jpeg','png'])
    return image

def show_image(image, boxes, txts, scores, font, save_image):
    st.image(image)
    im_show = draw_ocr(image, boxes, txts, scores, font_path=f'./fonts/{font}')
    im_show = Image.fromarray(im_show)
    if save_image:
        im_show.save('result.jpg')  
    st.image(im_show)

def main():
    lang = select_language()
    image = select_image()

    st.sidebar.header('Configuration')
    outputsize = st.sidebar.selectbox('Output Size', [384,512,768])
    save_image = st.sidebar.checkbox('Save image',value=True) 

    if image is not None:
        image = image.read()
        image = tf.image.decode_image(image, channels=3).numpy()
        ocr, font = get_model(lang)
        # image = tf.image.resize(image, 
        #                 [outputsize, outputsize],
        #                 method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
        # image =  image.numpy()
        result = ocr.ocr(image, cls=True)
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        show_image(image, boxes, txts, scores, font, save_image)

if __name__ == '__main__':
    main()