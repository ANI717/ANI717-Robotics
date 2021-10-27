## Install Dependency
Install `Inputs`, `Torch`, `Torchvision`, `Opencv`, `traitlets`, `multiexit`, `Adafruit-SSD1306` and `Adafruit_MotorHat`.<br/>
```
python3 -m pip install inputs torch torchvision opencv-python
python3 -m pip install Adafruit-SSD1306 Adafruit_MotorHat traitlets multiexit
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
colcon build --symlink-install && . install/setup.bash && ros2 launch robot_launch gamepad_launch.py
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
