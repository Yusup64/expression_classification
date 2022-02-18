""" import torch
import numpy as np
from torchvision import models """
import os
mypath = os.path.abspath(os.path.join(os.getcwd(), '../Basic/static/new.jpg'))
print(mypath)
""" x = torch.zeros(5, 3, dtype=torch.long)
print('当前的矩阵：',x.size())
print(x)
 """
#! tensor转numpy
""" x = torch.ones(5)
print(x.numpy()) """

#! numpy转tensor
""" x = np.ones(5)
print(torch.from_numpy(x))
 """
# print(torch.randn(3, 5, requires_grad=True))
