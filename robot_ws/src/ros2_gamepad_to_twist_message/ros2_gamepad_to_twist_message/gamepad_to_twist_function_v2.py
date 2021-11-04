#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ROS2 Gamepad to Twist Message Publish Executable.

This script publishes gamepad controller data to "\cmd_vel" topic as Twist 
message.

Revision History:
        2021-10-01 (Animesh): Baseline Software.

Example:
        $ colcon build && source install/setup.bash && ros2 run ros2_gamepad_to_twist_message execute
        $ source install/setup.bash && ros2 run ros2_gamepad_to_twist_message execute
        $ ros2 run ros2_gamepad_to_twist_message execute

"""


#___Import Modules:
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

from inputs import get_gamepad


#___Global Variables:
PUBLISH_TOPIC = '/cmd_vel'


#__Classes
class GamepadTwist(Node):
    """Gamepad Twist Class.
    
    This class contains all methods to publish gamepad controller data. 
    
    """

    def __init__(self):
        super().__init__('gamepad_publisher')
        self.publisher_ = self.create_publisher(Twist, PUBLISH_TOPIC, 10)
        timer_period = 0.01
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        # initialization
        self.max_z = 1
        self.max_x = 1
        self.z = 0.0
        self.x = 0.0

    def timer_callback(self):
        """Timer Callback Function
        
        This method publishes data as Twist message.
        
        """

        # initializes Twist message
        twist = Twist()
        
        events = get_gamepad()
        for event in events:
            if event.code == 'ABS_Z':
                self.max_z = max(abs(event.state), self.max_z)
                self.z = round((event.state/self.max_z)*2 - 1, 1)
            
            if event.code == 'ABS_Y':
                self.max_x = max(abs(event.state), self.max_x)
                self.x = round(-((event.state/self.max_x)*2 - 1), 1)
                
        # creates Twist message
        twist.angular.z = self.z
        twist.linear.x = self.x

        # publishes message
        self.publisher_.publish(twist)
        self.get_logger().info("Angular Z: {:.2f}, Linear X: {:.2f}".format(self.z, self.x))

        return None


def main(args=None):
    """This is the Main Method.
    
    """
    
    # initializes node and start publishing
    rclpy.init(args=args)
    gamepad_publisher = GamepadTwist()
    rclpy.spin(gamepad_publisher)
    
    # shuts down and releases everything
    gamepad_publisher.destroy_node()
    rclpy.shutdown()
    
    return None


if __name__ == '__main__':
    main()


#                                                                              
# end of file
"""ANI717"""
