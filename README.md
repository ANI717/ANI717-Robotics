
<p align="center">
  <h1 align="center">ANI717 Robotics Workspace</h1>
</p>

## Download Workspace
```
git clone https://github.com/ANI717/ANI717_Robotics
```

## Add User to Inputs Group
```
sudo gpasswd -a $USER input
```

## Build Robot Workspace
```
cd ~/ANI717_Robotics/robot_ws/
rosws update
rosdep  install --from-paths src --ignore-src -r -y
colcon build && . install/setup.bash && ros2 launch ani717_robot gamepad_launch.py
```
