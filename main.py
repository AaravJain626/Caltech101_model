import torch
from torch import nn

import torchvision
from torchvision import datasets
from torchvision import transforms
from torchvision.transforms import ToTensor
import scipy
import numpy as np

device = 'cuda' if torch.cuda.is_available() else 'cpu'

