
<p align="center">
  <h1 align="center">ANI717 Robotics Workspace</h1>
</p>



## Build Robot Workspace
```
cd ~/ANI717_Robotics/robot_ws/
rosws update
rosdep  install --from-paths src --ignore-src -r -y
colcon build && . install/setup.bash && ros2 launch ani717_robot launch.py
```
