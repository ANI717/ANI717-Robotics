#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ROS2 Gamepad to Twist Launch Script.

This script moves Jetbot.

Revision History:
        2021-08-26 (Animesh): Baseline Software.

Example:
        $ colcon build && source install/setup.bash && ros2 launch ros2_keyboard_to_twist_message launch.py
        $ source install/setup.bash && ros2 launch ros2_keyboard_to_twist_message launch.py
        $ ros2 launch ros2_keyboard_to_twist_message launch.py

"""


#___Import Modules:
import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


#___Function:
def generate_launch_description():
    
    execute_cmd = Node(
        package = 'ros2_keyboard_to_twist_message',
        node_executable = 'execute')

        
    # Create the launch description and populate
    ld = LaunchDescription()
    
    # Add all actions
    ld.add_action(execute_cmd)
        
    return ld


#                                                                              
# end of file
"""ANI717"""
