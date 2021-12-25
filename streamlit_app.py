import io
import base64
from PIL import Image
import streamlit as st
import tensorflow as tf
from paddleocr import draw_ocr, PaddleOCR

@st.cache

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
    elif lang == 'Viet Nam':
        ocr = PaddleOCR(use_angle_cls=True, lang='vi')
        return ocr, 'arial.ttf'

def select_language():
    option = st.selectbox(
        'Choose language',
        ('Arabic', 'Welsh', 'Hindi', 'Nepali', 'Spanish', 'Tamil', \
        'English', 'Chinese', 'Korean', 'Japan', 'French', \
        'German', 'Italian', 'Viet Nam'))
    return option

def select_image():
    image = st.file_uploader("Upload your image here", type=['jpg','jpeg','png'])
    return image

def get_image_download_link(img,filename,text):
    buffered = io.BytesIO()
    img.save(buffered, format="png")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href =  f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
    return href

def show_image(image, boxes, txts, scores, font):
    st.image(image)
    im_show = draw_ocr(image, boxes, txts, scores, font_path=f'./fonts/{font}')
    im_show = Image.fromarray(im_show)
    st.image(im_show)
    st.sidebar.markdown(get_image_download_link(im_show,'image.png','Download '+'image.png'), unsafe_allow_html=True)

def main():
    lang = select_language()
    image = select_image()

    st.sidebar.header('Save image')

    if image is not None:
        image = image.read()
        image = tf.image.decode_image(image, channels=3).numpy()
        ocr, font = get_model(lang)
        result = ocr.ocr(image, cls=True)
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        show_image(image, boxes, txts, scores, font)


if __name__ == '__main__':
    st.markdown("<h1 style='text-align: center; color: black;'>OCR</h1>", unsafe_allow_html=True)
    main()