
<p align="center">
  <h1 align="center">ANI717 Robotics Workspace</h1>
</p>

Robotics workspace. Contains ROS2 packages to run robot cars controlled by gamepad, collects annotated camera images, and runs a robot car autonomously with a trained neural network.<br/>

## Colaborators
[Animesh Bala Ani](https://www.linkedin.com/in/ani717/)<br/>

## Demonstration <a name="demo"></a>
Demonstration of robot movement.<br/>
Direction: `Backward` `Left`.<br/>

<img src="https://github.com/ANI717/ani717_gif_repository/blob/main/ros2_twist_message_to_robot_motion/jetbot_motion.gif" alt="JupytarLab Interface" class="inline"/><br/>

## ROS2 Packages
[ros2-gamepad-to-twist-message](https://github.com/ANI717/ANI717_Robotics/tree/main/robot_ws/src/ros2-gamepad-to-twist-message)<br/>
[ros2-pytorch-model-to-twist-message](https://github.com/ANI717/ANI717_Robotics/tree/main/robot_ws/src/ros2-pytorch-model-to-twist-message)<br/>
[ros2-twist-message-to-robot-motion](https://github.com/ANI717/ANI717_Robotics/tree/main/robot_ws/src/ros2-twist-message-to-robot-motion)<br/>
[ros2-save-camera-image](https://github.com/ANI717/ANI717_Robotics/tree/main/robot_ws/src/ros2-save-camera-image)<br/>

## Download Workspace
```
git clone https://github.com/ANI717/ANI717_Robotics
cd ~/ANI717_Robotics/robot_ws/
```

## Install Dependency
Install `Inputs`, `Torch`, `Torchvision`, `Opencv`, `traitlets`, `multiexit`, `Adafruit-SSD1306` and `Adafruit_MotorHat`.<br/>
```
python3 -m pip install inputs torch torchvision opencv-python Adafruit-SSD1306 Adafruit_MotorHat traitlets multiexit
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
