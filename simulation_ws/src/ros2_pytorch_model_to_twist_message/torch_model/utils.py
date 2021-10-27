#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ANIMESH BALA ANI"""

# Import Modules
import torch
import config


# Load Checkpoint
def load_checkpoint(checkpoint_file, model, optimizer=None, lr=None):
    checkpoint = torch.load(checkpoint_file, map_location=config.DEVICE)
    model.load_state_dict(checkpoint["state_dict"])
    
    if optimizer:
        optimizer.load_state_dict(checkpoint["optimizer"])
    
        for param_group in optimizer.param_groups:
            param_group["lr"] = lr


# Prediction for Single Image
def single_prediction(model, image):
    return round(model(config.test_transforms(image=image)["image"].unsqueeze(0).to(config.DEVICE)).item())