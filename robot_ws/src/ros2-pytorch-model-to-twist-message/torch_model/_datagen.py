#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Race-car Deep Learning Utility Class.

This script contains data generator for deep learning session. 

Revision History:
        2020-12-25 (Animesh): Baseline Software.

Example:
        from _datagen import Datagen

"""


#___Import Modules:
import cv2
import numpy as np

import torch
from torch.utils.data import Dataset
import torchvision.transforms as transforms

from _parser import ParseData

#___Global Variables:
SHAPE = [100,100]


#__Classes:
class Datagen(Dataset):
    """Neural Network Data Generator.
    
    This class contains all methods to handle data generation for deep learning
    session.
    
    """

    def __init__(self, ilist=None, shape=SHAPE):
        """Constructor.
        
        Args:
            ilist (list): A list of input images.
            shape (list): A list containing image shape [width, height].

        """
        
        self.transform = transforms.Compose([transforms.ToTensor()])        
        self.ilist = ilist
        self.shape = shape        
        self.parsedata = ParseData()

        return None
    

    def get_image(self, image):
        """Image to Tensor converter.
        
        This method takes an image and returns as deep learning compatible 
        image tensor with proper transformation.
        
        Args:
            image (image file): Image as input.
        
        Returns:
            image (image tensor): Transformed image tensor.

        """
        
        # transform image with proper padding
        row, column, _ = image.shape
        image = cv2.copyMakeBorder(image, (column-row)//2, (column-row)//2, 
                                                   0, 0, cv2.BORDER_CONSTANT)
        
        # reshape image in proper size
        image = cv2.resize(image, (self.shape[0], self.shape[1]), \
                           interpolation=cv2.INTER_CUBIC)
        
        return self.transform(image)
    
    
    def get_label(self, label):
        """Tensor converter.
        
        This method takes an integer and converts it to tensor.
        
        Args:
            label (int): An input integer as label.
        
        Returns:
            label (tensor): label transformed to tensor.

        """

        return torch.from_numpy(np.array(label)).float()


    def __getitem__(self, index):
        """Getitem Method.
        
        This method takes image, servo and motor data and returns them as 
        deep learning compatible tensor with proper transformation.
        
        Args:
            index (int): An integer indicating required data index from 
            provided list.
        
        Returns:
            image (image tensor): Transformed image tensor.
            servo (tensor): Servo data in tensor form.
            motor (tensor): Motor data in tensor form.

        """
        
        # parse image, servo and motor data in tensor form
        iname = self.ilist["image"][index]
        image = self.get_image(self.parsedata.parse_image(iname))
        servo = self.get_label(self.parsedata.parse_servo(iname))
        motor = self.get_label(self.parsedata.parse_motor(iname))
        
        return image, servo, motor


    def __len__(self):
        """Len Method.
        
        This method returns the length of provided list.

        """
        
        return len(self.ilist)


#                                                                              
# end of file
"""ANI717"""