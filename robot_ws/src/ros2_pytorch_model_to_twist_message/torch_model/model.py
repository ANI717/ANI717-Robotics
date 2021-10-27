#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ANIMESH BALA ANI"""

# Import Modules
import numpy as np
import torch
import torch.nn as nn
import config


# NVidia Model Class
class NvidiaNet(nn.Module):
    def __init__(self, in_channels=3, shape=config.IMG_SHAPE):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(in_channels, 24, 5, stride=2),
            nn.ELU(),
            nn.Conv2d(24, 36, 5, stride=2),
            nn.ELU(),
            nn.Conv2d(36, 48, 5, stride=2),
            nn.ELU(),
            nn.Conv2d(48, 64, 3),
            nn.ELU(),
            nn.Conv2d(64, 64, 3),
            nn.Dropout(0.05),
        )

        self.flatsize = np.prod(self.features(torch.ones(1, 3, *shape)).size())

        self.classifier = nn.Sequential(
            nn.Linear(in_features=self.flatsize, out_features=100),
            nn.ELU(),
            nn.Linear(in_features=100, out_features=50),
            nn.ELU(),
            nn.Linear(in_features=50, out_features=10),
            nn.Linear(in_features=10, out_features=1),
        )
    
    def forward(self, x):
        x = self.features(x)
        x = x.view(-1, self.flatsize)
        x = self.classifier(x)

        return x