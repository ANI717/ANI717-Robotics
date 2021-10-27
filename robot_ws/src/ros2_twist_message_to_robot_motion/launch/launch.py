#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ROS2 Twist to Robot Motion Launch Script.

This script moves Jetbot.

Revision History:
        2021-08-26 (Animesh): Baseline Software.

Example:
        $ colcon build && source install/setup.bash && ros2 launch ros2_twist_to_robot_motion launch.py
        $ source install/setup.bash && ros2 launch ros2_twist_to_robot_motion launch.py
        $ ros2 launch ros2_twist_to_robot_motion launch.py

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
        package = 'ros2_twist_message_to_robot_motion',
        node_executable = 'execute')

        
    # Create the launch description and populate
    ld = LaunchDescription()
    
    # Add all actions
    ld.add_action(execute_cmd)
        
    return ld


#                                                                              
# end of file
"""ANI717"""
