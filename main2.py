import numpy as np
from PIL import Image#python image library
import matplotlib.pyplot as plt
import cv2

img=Image.open('./data/test.jpg')
print('Image')
print(img)

#matplotlib
img_mat=plt.imread("./data/test.jpg")
print('matplotlib')
print(img_mat)

#cv2
img_cv=cv2.imread('./data/test.jpg')
print('opencv')
print(img_cv)