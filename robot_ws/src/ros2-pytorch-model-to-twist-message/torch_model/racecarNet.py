#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Race-car Neural Network (Nvidia).

This script contains required deep learnling models.


Revision History:
        2020-03-15 (Dr. Bai): Baseline Train-test Model
        2020-03-15 (Animesh): Formatting, Commenting, Modified to make 
                              compatioble with any shape of image input
        2020-05-20 (Dr. Bai): Simpler Flat-size Calculator Implemented
        2020-05-20 (Animesh): More Simpler Flat-size Calculator Implemented
        2020-07-26 (Animesh): Updated Docstring

Example:
        from racecarNet import ServoNet, MotorNet

"""


#___Import Modules:
import numpy as np
import torch
from torch import nn


#___Global Variables:
SHAPE = [100,100] # [shape_y,shape_x]


#__Classes:
class ServoNet(nn.Module):
    """ServoNet Deep learning Model.

    This class contains deep learning model for prediction on servo data for 
    steering purposes.

    Inheritence:
        nn.Module: Base PyTorch class for all neural network modules.
    
    """

    def __init__(self, shape):
        """Constructor.

        Args:
            shape (list): A list containing image shape [width, height]

        Returns:
            None

        """

        super(ServoNet, self).__init__()

        self.features = nn.Sequential(
            nn.Conv2d(3, 24, 5, stride=2),
            nn.ELU(),
            nn.Conv2d(24, 36, 5, stride=2),
            nn.ELU(),
            nn.Conv2d(36, 48, 5, stride=2),
            nn.ELU(),
            nn.Conv2d(48, 64, 3),
            nn.ELU(),
            nn.Conv2d(64, 64, 3),
            nn.Dropout(0.25),
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

        return None


    def forward(self, x):
        """Forward Method to Make Prediction.
        
        This method passes tensors through neural network model.
        
        Args:
            x (tensor): Tensor converted input image data

        Returns:
            x (tensor): Prediction from neural network

        """

        x = self.features(x)
        x = x.view(-1, self.flatsize)
        x = self.classifier(x)

        return x


class MotorNet(nn.Module):
    """MotorNet Deep learning Model.
    
    This class contains deep learning model for prediction on motor data for 
    steering purposes.
    
    Inheritence:
        nn.Module: Base PyTorch class for all neural network modules.
    
    """

    def __init__(self, shape):
        """Constructor.
        
        Args:
            shape (list): A list containing image shape [width, height]

        Returns:
            None

        """
        
        super(MotorNet, self).__init__()     

        self.features = nn.Sequential(
            nn.Conv2d(3, 24, 3, stride=(2, 2)),
            nn.ELU(),
            nn.Conv2d(24, 36, 3, stride=(2, 2)),
            nn.ELU(),
            nn.Conv2d(36, 48, 3),
            nn.ELU(),
            nn.Conv2d(48, 64, 3),
            nn.ELU(),
            nn.Conv2d(64, 10, 3),
            nn.ELU(),
            nn.Dropout(0.25),
        )

        self.flatsize = np.prod(self.features(torch.ones(1, 3, *shape)).size())

        self.classifier = nn.Sequential(
            nn.Linear(self.flatsize, 10),
            nn.ELU(),
            nn.Linear(10, 1),
            nn.ELU(),
        )

        return None


    def forward(self, x):
        """Forward Method to Make Prediction.
        
        This method passes tensors through neural network model.
        
        Args:
            x (tensor): Tensor converted input image data

        Returns:
            x (tensor): Prediction from neural network

        """

        x = self.features(x)
        x = x.view(-1, self.flatsize)
        x = self.classifier(x)

        return x


#                                                                              
# end of file
"""ANI717"""