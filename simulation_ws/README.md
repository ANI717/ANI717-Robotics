## Install Dependency
Install `Torch`, `Torchvision`, `Albumentations`, `Opencv` and `Getch`.<br/>
```
python3 -m pip install torch torchvision opencv-python albumentations getch
```
Install ROS2 dependency.<br/>
```
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

## Build, Source & Launch Package (Keyboard)
```
cd ANI717_Robotics/simulation_ws/
export DISPLAY=:0
colcon build --symlink-install && . install/setup.bash && ros2 launch simulation_launch keyboard_launch.py
```

## Build, Source & Launch Package (Self Driving)
```
cd ANI717_Robotics/simulation_ws/
export DISPLAY=:0
colcon build --symlink-install && . install/setup.bash && ros2 launch simulation_launch autonomous_launch.py
```

## Zip Images for Download
```
cd ../
zip -r images.zip images
```
