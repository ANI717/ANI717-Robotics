#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Race-car Deep Learning Class.
This script contains all deep learning tools to train and predict speed and 
steering value from a provided image. 
Revision History:
        2020-05-10 (Animesh): Baseline Software.
        2020-07-30 (Animesh): Updated Docstring.
Example:
        from _train_test import NNTools
"""


#___Import Modules:
import json
import torch

from _datagen import Datagen
from racecarNet import ServoNet, MotorNet


#___Global Variables:
TYPE = ["servo", "test"]
SETTINGS = 'settings.json'
SEED = 717
WEIGHT = 'models/servo.pth'


#__Classes:
class NNTools:
    """Neural Network Tool Class.
    
    This class contains all methods to complete whole deep learing session
    containing training, testing and prediction-make sessions.
    
    """

    def __init__(self, settings=SETTINGS, types=TYPE, weight=WEIGHT):
        """Constructor.
        
        Args:
            settings (JSON file): Contains all settings manually provided.
            types (list): Contains settings to determine the session is for
                training or testing.
        """

        self.type = types[0]

        # set hyperparameters
        with open(settings) as fp:
            content = json.load(fp)[types[0]][types[1]]

            self.shape = content["shape"]
            self.batch_size = content["batch"]
            self.cuda = content["cuda"]

        # set neural net by type
        torch.manual_seed(SEED)
        if self.type == "servo":
            self.model = ServoNet(self.shape)
        elif self.type == "motor":
            self.model = MotorNet(self.shape)

        # load weights if required
        self.load_weights(weight)

        # set required classes
        self.datagen = Datagen(shape=self.shape)

        return None


    def load_weights(self, weights_path):
        """Mathod to load a Model.
        
        Args:
            weights_path (pth file): Pretrained Weights.
        """

        self.model.load_state_dict(torch.load(weights_path, \
                                             map_location=torch.device('cpu')))

        return None
    
    
    def predict(self, image):
        """Mathod for Prediction.
        
        This method predicts streering or speed value from a provided single
        image.
        
        Args:
            image (image file): Image as input.
        
        Returns:
            (int): Predicted steering or speed value.
        """

        image = self.datagen.get_image(image).unsqueeze(0)
        
        # implement GPU support if required
        if (self.cuda):
            model = self.model.cuda()
        else:
            model = self.model

        # return prediction
        if (self.cuda):
            return model(image.cuda()).round().int().item()
        else:
            return model(image).round().int().item()


#                                                                              
# end of file
"""ANI717"""
