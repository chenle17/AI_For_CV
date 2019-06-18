import torch
import torchvision
import torchvision.transforms as transforms

# 把PIL image或者numpy.ndarray转为tensor类型[0, 1]的图片,
# 归一化张量图片
transform = transforms.Compose(
    [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])