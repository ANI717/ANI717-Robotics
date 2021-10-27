#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ANIMESH BALA ANI"""

# Import Modules
import torch
import albumentations as A
from albumentations.pytorch import ToTensorV2


# Hyperparameters
TRAIN_TYPE = 'servo'

DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
NUM_WORKERS = 1
PIN_MEMORY = True

IMG_SHAPE = (75, 75) # height, width
IMG_CHANNELS = 3

BATCH_SIZE = 256
LEARNING_RATE = 1e-4
NUM_EPOCHS = 150

IMG_SOURCE = '../dataset/images'
TRAIN_CSV = '../dataset/train.csv'
TEST_CSV = '../dataset/test.csv'
VAL_CSV = '../dataset/val.csv'

LOAD_MODEL = False
SAVE_MODEL = True
WRITE_LOG = True

CHECKPOINT = "servo.pth.tar"
OUTPUT = 'output'

TOLERENCE = 1


# Transformations
train_transforms = A.Compose([
    A.Resize(height=IMG_SHAPE[0], width=IMG_SHAPE[1]),
    A.ColorJitter(p=0.2),
    A.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5], max_pixel_value=255.0,),
    ToTensorV2(),])

test_transforms = A.Compose([
    A.Resize(height=IMG_SHAPE[0], width=IMG_SHAPE[1]),
    A.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5], max_pixel_value=255.0,),
    ToTensorV2(),])