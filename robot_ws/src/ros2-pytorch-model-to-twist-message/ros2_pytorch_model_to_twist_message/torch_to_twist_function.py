#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ROS2 Pytorch Model to Twist Message Publish Executable.

This script subscribes to "\image" topic, reads image data, predicts servo 
and motor values, and publishes them in "\cmd_vel" topic as Twist message.
Robot Movement: Forward - Backword - Right - Left

Revision History:
        2021-04-01 (Animesh): Baseline Software.

Example:
        $ ros2 run ros2_pytorch_model_to_twist_message execute

"""


#___Import Modules:
import os
import sys
import numpy as np

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from ament_index_python.packages import get_package_share_directory

TORCH_MODEL = os.path.join(get_package_share_directory('ros2_pytorch_model_to_twist_message'), "torch_model")
sys.path.insert(1, TORCH_MODEL)

import config
from model import NvidiaNet
from utils import load_checkpoint, single_prediction


#___Global Variables:
DEEP_SETTINGS = os.path.join(TORCH_MODEL, 'settings.json')
SUBSCRIBE_TOPIC = '/image'
PUBLISH_TOPIC = '/cmd_vel'


#___Functions
def angular_calibration(servo, motor, ang_z, lin_x):
    """Angular Value Calibration Function
    
    This function generates proper angular value for robot movement.
    
    Args:
        servo (float): predicted servo/steering value.
        motor (float): predicted motor value.
        ang_z (float): previous angular value.
        lin_x (float): previous linear value
    
    Return:
        (float): current angular value
    
    """
    
    return 0.1*servo


def linear_calibration(servo, motor, ang_z, lin_x):
    """Linear Value Calibration Function
    
    This function generates proper linear value for robot movement.
    
    Args:
        servo (float): predicted servo/steering value.
        motor (float): predicted motor value.
        ang_z (float): previous angular value.
        lin_x (float): previous linear value
    
    Returns:
        (float): current linear value
    
    """
    
    return 0.1*motor


#__Classes
class DeeplearnTwist(Node):
    """Deeplearn Twist Class.
    
    This class contains all methods to read camera image and create Twist
    message using end to end learning method for robot movement. 
    
    """


    def __init__(self, servo_model, motor_model):
        """Constructor.
        
        Args:
            servo_model (object): servo/steering value prediction class object.
            motor_model (object): motor value prediction class object.
        
        """
        
        # initialize subscriber
        super().__init__('deeplearn_twist')
        self.subscription = self.create_subscription(Image, SUBSCRIBE_TOPIC, 
                                                     self.listener_callback, 1)
        self.subscription  # prevent unused variable warning
        
        # initialize publisher
        self.publisher_ = self.create_publisher(Twist, PUBLISH_TOPIC, 1)
        timer_period = 0.01  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        # initialize prediction classes
        self.servo_model = servo_model
        self.motor_model = motor_model
        
        # initialize servo and motor value
        self.servo = 5
        self.motor = 5


    def listener_callback(self, msg):
        """Listener Callback Function
        
        This method subscribes to image topic and reads image data.
        
        """

        # parses data from subscribed topic message
        height = msg.height
        width = msg.width
        channel = msg.step//msg.width
        frame = np.reshape(msg.data, (height, width, channel))
        
        # makes prediction for servo and motor value from neural network
        self.servo = single_prediction(self.servo_model, frame)
        self.motor = single_prediction(self.motor_model, frame)
        
        self.get_logger().info("Servo: %d, Motor: %d" % (self.servo, self.motor))
        
        return None


    def timer_callback(self):
        """Timer Callback Function
        
        This method publishes servo and motor data as Twist message.
        
        """

        # initializes Twist message
        twist = Twist()

        # creates Twist message
        twist.angular.z = angular_calibration(self.servo, self.motor, twist.angular.z, twist.linear.x)
        twist.linear.x = linear_calibration(self.servo, self.motor, twist.angular.z, twist.linear.x)

        # publishes message
        self.publisher_.publish(twist)
        self.get_logger().info("Servo: %d, Motor: %d" % (self.servo, self.motor))

        return None


#___Main Method:   
def main(args=None):
    """This is the Main Method.
    
    This method contains testing session to predict speed and steering value.
    
    """

    # initialize prediction classes
    servo_model = NvidiaNet(in_channels=3).to(config.DEVICE)
    load_checkpoint(os.path.join(TORCH_MODEL, config.CHECKPOINT), servo_model)
    servo_model.eval()
    motor_model = NvidiaNet(in_channels=3).to(config.DEVICE)
    load_checkpoint(os.path.join(TORCH_MODEL, config.CHECKPOINT), motor_model)
    motor_model.eval()

    # initializes node and start publishing
    rclpy.init(args=args)
    deeplearn_twist = DeeplearnTwist(servo_model, motor_model)
    rclpy.spin(deeplearn_twist)

    # shuts down and releases everything
    deeplearn_twist.destroy_node()
    rclpy.shutdown()

    return None


#___Driver Program:
if __name__ == '__main__':
    main()


#                                                                              
# end of file
"""ANI717"""
