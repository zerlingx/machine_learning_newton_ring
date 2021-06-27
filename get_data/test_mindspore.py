import mindspore.dataset as ds
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from numpy.lib.type_check import imag

np.random.seed(58)

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

class DatasetGenerator:
    def __init__(self):
        img1 = get_img('get_data/grey_UNE_avatar.jpg')
        img2 = get_img('get_data/Figure1.jpg')
        img = np.stack((img1,img2))
        self.data = img
        ct1 = [20,30]
        ct2 = [40,50]
        ct = np.stack((ct1,ct2))
        self.label = ct

    def __getitem__(self, index):
        return self.data[index], self.label[index]

    def __len__(self):
        return len(self.data)

dataset_generator = DatasetGenerator()
dataset = ds.GeneratorDataset(dataset_generator, ["data", "label"], shuffle=False)

for data in dataset.create_dict_iterator():
    print('{}'.format(data["data"]), '{}'.format(data["label"]))
