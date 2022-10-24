import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# img = cv2.imread(r'C:\Users\harez\OneDrive\Pulpit\PythonOOP\MachineLearningMateuszHareza\surf.jpg')
# img = cv2.resize(img, (720, 480))
# cv2.imshow('Result', img)
# cv2.waitKey(0)

img = r'C:\Users\harez\OneDrive\Pulpit\PythonOOP\MachineLearningMateuszHareza\surf.jpg'
def convertImageToString(img):
    img = cv2.imread(img)
    print(pytesseract.image_to_string(img))



convertImageToString(img)