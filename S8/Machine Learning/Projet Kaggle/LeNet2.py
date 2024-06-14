import torch
import torch.nn as nn
import torch.nn.functional as F

class LeNet2(nn.Module):

    def __init__(self):
        super(LeNet2, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, kernel_size=5, padding=2)
        self.conv2 = nn.Conv2d(6, 16, kernel_size=5)
        self.fc1   = nn.Linear(62*62*16, 120)
        self.fc2   = nn.Linear(120, 84)
        self.fc3   = nn.Linear(84, 4)
    
    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), kernel_size=(2, 2), stride=2)
        x = F.max_pool2d(F.relu(self.conv2(x)), kernel_size=(2, 2), stride=2)
        x = nn.Flatten()(x)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        x = self.dropout(x)
        return x
    
    def num_flat_features(self, x):
        size = x.size()[1:]  # toutes les dimensions sauf celle du batch
        num_features = 1
        for s in size:
            num_features *= s
        return num_features