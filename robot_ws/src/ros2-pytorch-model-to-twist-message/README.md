<p align="center">
  <h1 align="center">ROS 2 Deep Learning Package for Robot Movement</h1>
</p>

ROS 2 Package to Publish Twist Message from Subscribed Sensor Image Message using End to End Learning (Deep Learning) Method for Robot Movement.

## Colaborators
[Animesh Bala Ani](https://www.linkedin.com/in/ani717/)

## Install Dependency
Install Torch, Torchvision and Opencv.
```
python3 -m pip install torch torchvision opencv-python
```
Install ROS2 dependency.
```
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

## Build, Source & Run Package
ros2 run ros2_pytorch_model_to_twist_message execute
```
colcon build && . install/setup.bash && ros2 run ros2_pytorch_model_to_twist_message execute
```

## Launch Package
ros2 launch ros2_pytorch_model_to_twist_message launch.py
```
colcon build && . install/setup.bash && ros2 launch ros2_pytorch_model_to_twist_message launch.py
```

## ROS 2 Package to capture image with camera
This ROS 2 built-in package can be used to capture image with a camera. It publishes captured images to ROS 2 /image topic. The ros2_deeplearn_twist package subscribes to this topic and creates twist message.
```
ros2 run image_tools cam2image
```
