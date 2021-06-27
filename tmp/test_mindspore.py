from cv2 import data
import mindspore.dataset as ds
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from numpy import random
from numpy.lib.type_check import imag

def get_color_channels(img):
    img = img.copy()
    channels_num = len(img.shape)
    result = []
    
    channels = np.split(img, channels_num, axis=2)
    for i in channels:
        result.append(i.sum(axis=2)) 
    return result

class DatasetGenerator:
    def __init__(self):
        img = np.array(Image.open("data/img/train_img_1.jpg"))
        path = "data/img/train_img_"
        img1 = np.array(Image.open("data/img/train_img_1.jpg"))
        img = np.stack((img,img1))
        for img_i in range(3049):
            img_nxt = np.array(Image.open(path+str(img_i+2)+".jpg"))
            img_nxt = img_nxt[np.newaxis, :]
            img = np.vstack((img, img_nxt))
        self.data = img
        ct = np.load("data/center/center.npy")
        self.label = ct

    def __getitem__(self, index):
        return self.data[index], self.label[index]

    def __len__(self):
        return len(self.data)

dataset_generator = DatasetGenerator()
dataset = ds.GeneratorDataset(dataset_generator, ["data", "label"], shuffle=False)

print("\n01 ---dataset generate complete---\n")

# 全部打印
# for data in dataset.create_dict_iterator():
#     print('{}'.format(data["data"]), '{}'.format(data["label"]))

p_data = dataset.create_dict_iterator()

num = random.randint(1,3050)
print('{}'.format(p_data[num]["data"]), '{}'.format(data[num]["label"]))

plt.imshow(p_data[num]["data"])
plt.scatter(int(p_data[num]["label"][0]), int(p_data[num]["label"][1]), color='r',s=20)
plt.show()
