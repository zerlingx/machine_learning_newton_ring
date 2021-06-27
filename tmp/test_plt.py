import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def get_color_channels(img):
    img = img.copy()
    channels_num = len(img.shape)
    result = []
    
    channels = np.split(img, channels_num, axis=2)
    for i in channels:
        result.append(i.sum(axis=2)) 
    return result

# 读取图像，转为numpy数组，显示
img = Image.open('get_data/img_1.jpg')
# img = Image.open('get_data/grey_UNE_avatar.jpg')
img = np.array(img)
# plt.imshow(img)
# plt.colorbar()
# plt.show()

# 变为灰度图
R, G, B, = get_color_channels(img)
L = R * 299 / 1000 + G * 587 / 1000 + B * 114 / 1000
#中心
ct = np.array(L.shape)/2
plt.scatter(int(ct[0]), int(ct[1]), color='r',s=20)

# plt.imshow(L, cmap="gray")
# plt.colorbar()
# plt.show()

# 灰度图L，一个numpy数组
# print(L)
