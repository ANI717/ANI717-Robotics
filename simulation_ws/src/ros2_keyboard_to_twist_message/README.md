<p align="center">
  <h1 align="center">ROS 2 Deep Learning Package for Robot Movement</h1>
</p>

ROS 2 Package to Publish Gamepad Controller Inputs to Twist Message for Robot Movement.<br/>

## Install Dependency
Install `Keyboard`.<br/>
```
python3 -m pip install keyboard
```
Install ROS2 dependency.<br/>
```
rosdep update
rosdep install --from-paths src --ignore-src -r -y

## Build, Source & Run Package
```
colcon build && . install/setup.bash && ros2 run ros2_keyboard_to_twist_message execute
```

## Launch Package
```
colcon build && . install/setup.bash && ros2 launch ros2_keyboard_to_twist_message launch.py
```
