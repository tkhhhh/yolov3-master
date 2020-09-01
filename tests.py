import torch

from torch.backends import cudnn

a = torch.tensor(1.)
print(cudnn.is_acceptable(a.cuda()) )