import torch
from torch import nn
import torch.nn.functional as F
import torch_optimizer as optim 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

class LinearModel(nn.Module):
    def 