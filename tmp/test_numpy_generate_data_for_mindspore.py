import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from numpy.core.shape_base import stack
from numpy.lib.type_check import imag

def get_color_channels(img):
    img = img.copy()
    channels_num = len(img.shape)
    result = []
    
    channels = np.split(img, channels_num, axis=2)
    for i in channels:
        result.append(i.sum(axis=2)) 
    return result

def get_img(path):
    img = Image.open(path)
    # w, h = img.size
    # print(w,h)
    box = (0, 0, 224, 224)
    img = img.crop(box) 
    img = np.array(img)
    R, G, B, = get_color_channels(img)
    L = R * 299 / 1000 + G * 587 / 1000 + B * 114 / 1000
    return L

#图像数组
img1 = get_img('get_data/grey_UNE_avatar.jpg')
img2 = get_img('get_data/Figure1.jpg')
img = np.stack((img1,img2))

#坐标数组
ct1 = [20,30]
ct2 = [40,50]
ct = np.stack((ct1,ct2))
a = np.array([[20,30],[40,50]])

print(img)
print(a)

# 图像的堆叠法，先升维，再用vstack
x=img1[np.newaxis, :]
img = np.vstack((img, x))

# 坐标的堆叠法，可以直接用vstack
a = np.vstack((a,[60,70]))

print("\n各增加一组")
print(img)
print(a)
