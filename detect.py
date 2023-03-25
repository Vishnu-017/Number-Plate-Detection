from paddleocr import PaddleOCR, draw_ocr
import cv2
import numpy as np
ocr = PaddleOCR(lang = 'en')
image_path = 'detections.jpg'
image_cv = cv2.imread(image_path)
image_height = image_cv.shape[0]
image_width = image_cv.shape[1]
print(image_height,image_width)
output = ocr.ocr(image_path)
print(output)
print(len(output))
arr2d = np.array(output)
arr1d = arr2d.flatten()
print(arr1d[1][0]) 
number = arr1d[1][0]
print(number)
