import torch
from torch import nn

import torchvision
from torchvision import datasets
from torchvision import transforms
from torchvision.transforms import ToTensor
import scipy
import numpy as np

device = 'cuda' if torch.cuda.is_available() else 'cpu'

data = torchvision.datasets.Caltech101(
    root = "data",
    download = True,
    transform = ToTensor(),
    target_transform = None
)
     

# train test split
train_data = data[int(len(data) * 0.8)]
len(x)
     
2

len(train_data)
     
