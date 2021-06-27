# machine_learning_newton_ring

>机器学习课程大作业“基于深度学习的条纹分析”，即用深度学习算法进行牛顿环干涉图像的中心坐标估算。  
实验平台：win10、华为云Ascend  
主要编程工具：matlab、python、mindspore  

## 数据生成

没有实际的实验图像，因此根据牛顿环的原理和公式用matlab生成（详见[get_NTR.m](get_data/get_NTR.m)），保存在[raw_NTR_img](raw_NTR_img)，共61张。

生成的图像尺寸为$278\times278$，用python进行剪裁、添加噪声（详见[proceed_raw_img.py](get_data/proceed_raw_img.py)），变为$224\times224\times1$的灰度图，保存在[data/img](data/img)，共3050张，占54.6M。

中心坐标以numpy数组文件的形式保存为[center.npy](data/center/center.npy)，ct\[num\]即第num张图片的中心坐标。
