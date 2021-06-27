import numpy as np
import random
import matplotlib.pyplot as plt
from PIL import Image

num = random.randint(1,3050)
path = "data/img/train_img_"+str(num)+".jpg"
img = Image.open(path)
img = np.array(img)
ct = np.load("data/center/center.npy")

plt.imshow(img, cmap="gray")
plt.scatter(int(ct[num][0]), int(ct[num][1]), color='r',s=20)
plt.colorbar()
plt.title(path+"  ct:"+str(ct[num][0])+","+str(ct[num][1]))
plt.show()
