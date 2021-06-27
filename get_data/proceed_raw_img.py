import numpy as np
import random
import matplotlib.pyplot as plt
from PIL import Image
import skimage
from skimage import util
from skimage.util import noise
import cv2

def get_color_channels(img):
    img = img.copy()
    channels_num = len(img.shape)
    result = []
    
    channels = np.split(img, channels_num, axis=2)
    for i in channels:
        result.append(i.sum(axis=2)) 
    return result

def proceed_and_output(input_path, output_path):
    #导入图像
    # input_path = "get_data/img_1.jpg"
    img = Image.open(input_path)

    #随机裁剪
    x = random.randint(0,54)
    y = random.randint(0,54)
    box = (x, y, 224+x, 224+y)
    img = img.crop(box)
    img = np.array(img)
    # print(img)

    #添加噪声
    noise = util.random_noise(img,mode='s&p',amount=0.003)
    img = 255*noise

    # 变为灰度图
    R, G, B, = get_color_channels(img)
    L = R * 299 / 1000 + G * 587 / 1000 + B * 114 / 1000

    #画出中心
    ct = [139-x, 139-y]
    plt.scatter(int(ct[0]), int(ct[1]), color='r',s=20)

    plt.imshow(L, cmap="gray")
    plt.axis('off')
    # plt.colorbar()
    # plt.show()

    # print(L)

    # 输出添加了噪声的灰度图片
    # 输出的图片应当为224*224*1的灰度图
    # output_path="get_data/noised_1.jpg"
    cv2.imwrite(output_path, L)
    #返回中心坐标ct，方便起见，在主函数里并成一个numpy数组保存
    return ct

cnt = 0
for img_i in range(61):
    input_path = "raw_NTR_img/img_"+str(img_i+1)+".jpg"
    for out_i in range(50):
        cnt += 1
        output_path = "data/img/train_img_"+str(cnt)+".jpg"
        ct_tmp = proceed_and_output(input_path, output_path)
        if cnt == 1:
            ct = np.array([ct_tmp])
        else:
            ct = np.vstack((ct,ct_tmp))
#保存中心坐标
np.save("data/center/center.npy",ct)
