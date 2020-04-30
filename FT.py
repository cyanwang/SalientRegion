import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
# from optimize import contoursCollection
 
img = cv2.imread(r"13.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.GaussianBlur(img,(5,5), 0)
gray_lab = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
print(gray_lab)
l_mean = np.mean(gray_lab[:,:,0])
a_mean = np.mean(gray_lab[:,:,1])
b_mean = np.mean(gray_lab[:,:,2])
lab = np.square(gray_lab- np.array([l_mean, a_mean, b_mean]))
lab = np.sum(lab,axis=2)
lab = lab/np.max(lab)
print(lab)
 
# rectList=contoursCollection(lab)
cv2.imshow("lab",lab)
 
cv2.waitKey(0)
# plt.imshow(lab, cmap='gray')
# plt.show()
