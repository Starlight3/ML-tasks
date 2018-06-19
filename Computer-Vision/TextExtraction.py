from PIL import Image
import pytesseract
import cv2
import os

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
#TESSDATA_PREFIX='C:\Program Files (x86)\Tesseract-OCR'

image = cv2.imread('test.jpg')
'''
new = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
new[:,:,2] += 10
new = cv2.cvtColor(new, cv2.COLOR_HSV2BGR)'''
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] 
#gray = cv2.medianBlur(gray, 3)

cv2.imshow('img',gray)
cv2.imwrite('Rendered Document.jpg', gray)
text = pytesseract.image_to_string(gray, lang='eng', config='--psm 11')
print(text)
