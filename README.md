
<p align="center">
  <h1 align="center">ANI717 Robotics Workspace</h1>
</p>

Robotics workspace. Contains ROS2 packages to run robot cars controlled by gamepad, collects annotated camera images, and runs a robot car autonomously with a trained neural network.<br/>

[Computer Vision & Deep Learning Repository.](https://github.com/ANI717/Self_Driving_CV_Repository)

## Colaborators
[Computer Fusion Laboratory (CFL) - Temple University College of Engineering](https://sites.temple.edu/cflab/people/)
* [Animesh Bala Ani](https://www.linkedin.com/in/ani717/)<br/>
* [Michael Nghe](https://sites.temple.edu/cflab/people/)<br/>
* [Dr. Li Bai](https://engineering.temple.edu/about/faculty-staff/li-bai-lbai)<br/>

## ROS2 Packages
[ros2_pytorch_model_to_twist_message](https://github.com/ANI717/ANI717_Robotics/tree/main/robot_ws/src/ros2_pytorch_model_to_twist_message)<br/>
[ros2_save_camera_image](https://github.com/ANI717/ANI717_Robotics/tree/main/robot_ws/src/ros2_save_camera_image)<br/>

[ros2_gamepad_to_twist_message](https://github.com/ANI717/ANI717_Robotics/tree/main/robot_ws/src/ros2_gamepad_to_twist_message)<br/>
[ros2_twist_message_to_robot_motion](https://github.com/ANI717/ANI717_Robotics/tree/main/robot_ws/src/ros2_twist_message_to_robot_motion)<br/>

[ros2_keyboard_to_twist_message](https://github.com/ANI717/ANI717_Robotics/tree/main/simulation_ws/src/ros2_keyboard_to_twist_message)<br/>
[ros2_world_simulation](https://github.com/ANI717/ANI717_Robotics/tree/main/simulation_ws/src/ros2_world_simulation)<br/>
[ros2_robot_simulation](https://github.com/ANI717/ANI717_Robotics/tree/main/simulation_ws/src/ros2_robot_simulation)<br/>

## Download Workspace
```
git clone https://github.com/ANI717/ANI717_Robotics
cd ~/ANI717_Robotics/robot_ws/
```

## Install Dependency
Install `Inputs`, `Torch`, `Torchvision`, `Opencv`, `traitlets`, `multiexit`, `Adafruit-SSD1306` and `Adafruit_MotorHat`.<br/>
```
python3 -m pip install inputs torch torchvision opencv-python
python3 -m pip install Adafruit-SSD1306 Adafruit_MotorHat traitlets multiexit
```
Install ROS2 dependency.<br/>
```
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

## Add User to Input Group
Run following command and reboot.<br/>
```
sudo gpasswd -a $USER input
```

## Build, Source & Launch Package (Gamepad)
```
colcon build && . install/setup.bash && ros2 launch robot_launch gamepad_launch.py
colcon build --symlink-install && . install/setup.bash && ros2 launch robot_launch gamepad_launch.py
```

## Build, Source & Launch Package (Self Driving)
```
colcon build && . install/setup.bash && ros2 launch robot_launch autonomous_launch.py
```

## Zip Images for Download
```
cd ../
zip -r images.zip images
```
