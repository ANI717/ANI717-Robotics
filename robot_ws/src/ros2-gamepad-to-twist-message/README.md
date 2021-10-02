<p align="center">
  <h1 align="center">ROS 2 Deep Learning Package for Robot Movement</h1>
</p>

ROS 2 Package to Publish Gamepad Controller Inputs to Twist Message for Robot Movement.<br/>

## Install Dependency
Install `Inputs`.<br/>
```
python3 -m pip install inputs
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

## Build, Source & Run Package
```
colcon build && . install/setup.bash && ros2 run ros2_gamepad_to_twist_message execute
```

## Launch Package
```
colcon build && . install/setup.bash && ros2 launch ros2_gamepad_to_twist_message launch.py
```
