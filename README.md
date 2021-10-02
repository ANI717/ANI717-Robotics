
<p align="center">
  <h1 align="center">ANI717 Robotics Workspace</h1>
</p>

## Colaborators
[Animesh Bala Ani](https://www.linkedin.com/in/ani717/)<br/>

## Download Workspace
```
git clone https://github.com/ANI717/ANI717_Robotics
```

## Add User to Input Group
Run following command and reboot.<br/>
```
sudo gpasswd -a $USER input
```

## Build Robot Workspace
```
cd ~/ANI717_Robotics/robot_ws/
rosws update
rosdep  install --from-paths src --ignore-src -r -y
colcon build && . install/setup.bash && ros2 launch robot_launch gamepad_launch.py
```
