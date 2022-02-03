import cv2
img_cv=cv2.imread('./data/test.jpg')
print(img_cv.shape)

#BGR
import matplotlib.pyplot as plt
#%matplotlib inline
plt.imshow(img_cv)
