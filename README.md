
<p align="center">
  <h1 align="center">ANI717 Robotics Workspace</h1>
</p>

## Download Package
Download package in a ROS workspace.
```
git clone https://github.com/ANI717/ANI717_Robotics
```

## Build Robot Workspace
```
cd ~/ANI717_Robotics/robot_ws/
rosws update
rosdep  install --from-paths src --ignore-src -r -y
colcon build && . install/setup.bash && ros2 launch ani717_robot gamepad_launch.py
```
