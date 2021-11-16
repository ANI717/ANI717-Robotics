<p align="center">
  <h1 align="center">ANI717 Simulation Workspace</h1>
</p>

<img src="https://github.com/ANI717/ANI717_Robotics/blob/main/Simulation%20Workspace.png" alt="Simulation Workspace Diagram" class="inline"/><br/>

## Colaborators
[Animesh Bala Ani](https://www.linkedin.com/in/ani717/)

## Table of Contents
* [Install Dependency](#install) <br/>
* [Build, Source & Launch Package (Keyboard)](#keyboard) <br/>
* [Build, Source & Launch Package (Self Driving))](#self) <br/>
* [Launch Arguments](#arg) <br/>
* [Zip Images for Download](#zip) <br/>


## Install Dependency <a name="install"></a>
Install `Torch`, `Torchvision`, `Albumentations`, `Opencv` and `Getch`.<br/>
```
python3 -m pip install torch torchvision opencv-python albumentations getch
```
Install ROS2 dependency.<br/>
```
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```


## Build, Source & Launch Package (Keyboard) <a name="keyboard"></a>
Terminal 1
```
cd ANI717_Robotics/simulation_ws/
export DISPLAY=:0
colcon build --symlink-install && source install/local_setup.bash && ros2 launch simulation_app keyboard_launch.py
```

Terminal 2 (Run following commands and select `/image` as `Image View`
```
export DISPLAY=:0
rqt
```


Terminal 3
```
cd ANI717_Robotics/simulation_ws/
source install/local_setup.bash && ros2 run ros2_keyboard_to_twist_message execute
```


## Build, Source & Launch Package (Self Driving) <a name="self"></a>
```
cd ANI717_Robotics/simulation_ws/
export DISPLAY=:0
colcon build --symlink-install && source install/local_setup.bash && ros2 launch simulation_app autonomous_launch.py
```


## Zip Images for Download <a name="zip"></a>
```
cd ../
zip -r images.zip images
```
