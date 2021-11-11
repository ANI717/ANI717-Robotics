<p align="center">
  <h1 align="center">A Generalized ROS 2 Package to Publish Gamepad Data as Twist Message</h1>
</p>

ROS 2 Package to Publish Gamepad Controller Data as Twist Message for Robot Movement.<br/>

## Colaborators
[Animesh Bala Ani](https://www.linkedin.com/in/ani717/)

## Key Mapping <a name="key"></a>
`Left Joystick Up`:`+ linear.x`<br/>
`Left Joystick Down`:`- linear.x`<br/>
`Right Joystick Right`:`+ angular.z`<br/>
`Right Joystick Left`:`- angular.z`<br/>

`linear.x range`:`-1 to +1`<br/>
`angular.z range`:`-1 to +1`<br/>

## Install Dependency
Install `Inputs`.<br/>
```
python3 -m pip install inputs
```
Install ROS2 dependency.<br/>
```
sudo apt-get update
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

## Add User to Input Group
Run following command and reboot.<br/>
```
sudo gpasswd -a $USER input
```

## Build, Source & Launch Package
```
colcon build --symlink-install --packages-select ros2_gamepad_to_twist_message
source install/local_setup.bash
ros2 launch ros2_gamepad_to_twist_message launch.py
```
```
colcon build --symlink-install && source install/local_setup.bash && ros2 launch ros2_gamepad_to_twist_message launch.py
```

## Miscellaneous
Select Gamepad type from `logitech` or `waveshare` by editing `line 31` of `launch/launch.py` file.<br/>
Or use this names as arguments for `gamepad_type`.<br/>
Default `gamepad_type`:`logitech`<br/> 

Edit `settings.json` file to assign `publish topic` and `publish frequency`.<br/>
Default `publish topic`:`\cmd_vel`<br/> 
Default `publish frequency`:`100`<br/>
