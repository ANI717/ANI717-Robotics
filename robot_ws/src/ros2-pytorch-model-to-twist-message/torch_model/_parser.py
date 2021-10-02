#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Race-car Deep Learning Utility Class.

This script contains data parsing tools from given image name. 

Revision History:
        2020-12-25 (Animesh): Baseline Software.

Example:
        from _parser import ParseData

"""


#___Import Modules:
import cv2


#___Global Variables:
SHAPE = [100,100]


#__Classes:
class ParseData:
    """Data Parser Class
    
    This class contains all tools to parse servo, motor and image data from a 
    given list item.
    
    """

    def __init__(self):
        """Constructor.

        """

        return None


    def parse_data(self, fname):
        """Data Parser.
        
        This method parses data from a given file name.
        
        Args:
            fname (string): File name containing image directory along with 
                servo and motor value.

        Returns:
            (image file): Image file in opencv format.
            (int): Servo value.
            (int): Motor value.
        
        """
        
        return self.parse_image(fname), \
                    self.parse_servo(fname), self.parse_motor(fname)

    
    def parse_image(self, fname):
        """Image Parser.
        
        This method parses image from a given file name.
        
        Args:
            fname (string): File name containing image directory.

        Returns:
            (image file): Image file in opencv format.
        
        """
        
        return cv2.imread(fname)
    

    def parse_servo(self, fname):
        """Servo Data Parser.
        
        This method parses servo data from a given file name.
        
        Args:
            fname (string): File name containing image directory along with 
                servo and motor value.

        Returns:
            (int): Servo value.
        
        """
        
        return int(fname.split('.')[-2].split('_')[-2][1:3])
    

    def parse_motor(self, fname):
        """Motor Data Parser.
        
        This method parses motor data from a given file name.
        
        Args:
            fname (string): File name containing image directory along with 
                servo and motor value.

        Returns:
            (int): Motore value.
        
        """
        
        return int(fname.split('.')[-2].split('_')[-1][1:3])


#                                                                              
# end of file
"""ANI717"""