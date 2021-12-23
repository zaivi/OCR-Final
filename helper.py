from paddleocr import PaddleOCR

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