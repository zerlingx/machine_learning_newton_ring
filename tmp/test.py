import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from numpy.core.defchararray import center
import cv2

img = cv2.imread("data/img/train_img_1.jpg")
print(img.shape,img.size,img.dtype)
# cv2.imshow('src',img)
# cv2.waitKey()
print(img)