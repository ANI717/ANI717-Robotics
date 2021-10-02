#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ROS2 Image Saving Tool.

This script saves image with twist messages as annotation.

Revision History:
        2021-10-02 (Animesh): Baseline Software.

Example:
        $ colcon build && source install/setup.bash && ros2 run ros2_save_camera_image execute
        $ source install/setup.bash && ros2 run ros2_save_camera_image execute
        $ ros2 run ros2_save_camera_image execute

"""


#___Import Modules:
import os
from pathlib import Path
import numpy as np
import cv2
import datetime

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist


#___Global Variables:
SUBSCRIBE_TWIST_TOPIC = '/cmd_vel'
SUBSCRIBE_IMAGE_TOPIC = '/image'
IMAGE_FOLDER = '../images'
DATE_FOLDER = '{0:04d}-{1:02d}-{2:02d}-{3:02d}-{4:02d}'.format(datetime.datetime.now().year,
                                                               datetime.datetime.now().month,
                                                               datetime.datetime.now().day,
                                                               datetime.datetime.now().hour,
                                                               datetime.datetime.now().minute)


#__Classes
class ImageSubscriber(Node):
    """Image Saving Class.
    
    This class contains all methods to save image captured by camera. 
    
    """


    def __init__(self):
        super().__init__('image_subscriber')
        self.subscription1 = self.create_subscription(Image, SUBSCRIBE_IMAGE_TOPIC, 
                                                self.listener_callback1, 10)
        self.subscription1  # prevent unused variable warning
        self.image_count = 0
        
        self.subscription2 = self.create_subscription(Twist, SUBSCRIBE_TWIST_TOPIC,
                                                      self.listener_callback2, 10)
        self.subscription2
        self.x = 0
        self.z = 0
    

    def listener_callback1(self, msg):
        height = msg.height
        width = msg.width
        channel = msg.step//msg.width
        frame = np.reshape(msg.data, (height, width, channel))
        self.get_logger().info("Image Received")
        
        cv2.imwrite(os.path.join(IMAGE_FOLDER, DATE_FOLDER , '{0:07d}_servo_{1:02d}_motor_{2:02d}.jpg'.format(self.image_count, self.z, self.x)), frame)
        self.image_count += 1
    
    
    def listener_callback2(self, msg):        
        self.x = int(msg.linear.x*5) + 5
        self.z = int(msg.angular.z*5) + 5


#___Main Method:
def main(args=None):
    Path(os.path.join(IMAGE_FOLDER, DATE_FOLDER)).mkdir(parents=True, exist_ok=True)
    rclpy.init(args=args)
    image_subscriber = ImageSubscriber()
    rclpy.spin(image_subscriber)

    image_subscriber.destroy_node()
    rclpy.shutdown()


#___Driver Program:
if __name__ == '__main__':
    main()


#                                                                              
# end of file
"""ANI717"""
