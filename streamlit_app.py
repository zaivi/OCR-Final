import numpy as np
from PIL import Image
import streamlit as st
import tensorflow as tf
from paddleocr import draw_ocr, PaddleOCR


st.markdown("<h1 style='text-align: center; color: black;'>OCR</h1>", unsafe_allow_html=True)

def get_model(lang):
    if lang == 'English':
        ocr = PaddleOCR(use_angle_cls=True, lang='en')
        return ocr, 'simfang.ttf'
    elif lang == 'Arabic':
        ocr = PaddleOCR(use_angle_cls=True, lang='ar')
        return ocr, 'arabic.ttf'
    elif lang == 'Welsh':
        ocr = PaddleOCR(use_angle_cls=True, lang='cy')
        return ocr, 'cyrillic.ttf'
    elif lang == 'Hindi':
        ocr = PaddleOCR(use_angle_cls=True, lang='hi')
        return ocr, 'hindi.ttf'
    elif lang == 'Nepali':
        ocr = PaddleOCR(use_angle_cls=True, lang='ne')
        return ocr, 'nepali.ttf'
    elif lang == 'Spanish':
        ocr = PaddleOCR(use_angle_cls=True, lang='es')
        return ocr, 'spanish.ttf'
    elif lang == 'Tamil':
        ocr = PaddleOCR(use_angle_cls=True, lang='ta')
        return ocr, 'tamil.ttf'
    elif lang == 'Chinese':
        ocr = PaddleOCR(use_angle_cls=True, lang='ch')
        return ocr, 'simfang.ttf'
    elif lang == 'Japan':
        ocr = PaddleOCR(use_angle_cls=True, lang='japan')
        return ocr, 'japan.ttc'
    elif lang == 'Korean':
        ocr = PaddleOCR(use_angle_cls=True, lang='korean')
        return ocr, 'korean.ttf'
    elif lang == 'French':
        ocr = PaddleOCR(use_angle_cls=True, lang='fr')
        return ocr, 'french.ttf'
    elif lang == 'German':
        ocr = PaddleOCR(use_angle_cls=True, lang='german')
        return ocr, 'german.ttf'
    elif lang == 'Italian':
        ocr = PaddleOCR(use_angle_cls=True, lang='it')
        return ocr, 'latin.ttf'

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