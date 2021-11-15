## Install Dependency
Install `Inputs` and `Adafruit_MotorHat`.<br/>
```
python3 -m pip install inputs Adafruit_MotorHat
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
cd ~/ANI717_Robotics/robot_ws/
colcon build --symlink-install && . install/setup.bash && ros2 launch robot_launch gamepad_launch.py
```

## Build, Source & Launch Package (Self Driving)
```
cd ~/ANI717_Robotics/robot_ws/
colcon build --symlink-install && . install/setup.bash && ros2 launch robot_launch autonomous_launch.py
```

## Zip Images for Download
```
cd ../
zip -r images.zip images
```
