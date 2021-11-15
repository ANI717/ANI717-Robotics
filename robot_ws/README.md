<p align="center">
  <h1 align="center">ANI717 Robot Workspace</h1>
</p>


## Colaborators
[Animesh Bala Ani](https://www.linkedin.com/in/ani717/)

## Table of Contents
* [Install Required Packages (Jetson Nano)](#jetson) <br/>
* [Install Dependency](#install) <br/>
* [Add User to Input Group](#user) <br/>
* [Build, Source & Launch Package (Gamepad)](#gamepad) <br/>
* [Build, Source & Launch Package (Self Driving))](#self) <br/>
* [Launch Arguments](#arg) <br/>
* [Zip Images for Download](#zip) <br/>

## Install Required Packages (Jetson Nano) <a name="jetson"></a>
Install `ROS2 Dashing`, `PyTorch`, `Torchvision`, `ONNXRuntime-GPU`, `Inputs` and `Adafruit_MotorHat`.<br/>
```
git clone https://github.com/ANI717/Headless-Jetson-Nano-Setup
cd ~/Headless-Jetson-Nano-Setup
chmod +x ./dashing.sh && ./dashing.sh
chmod +x ./pytorch.sh && ./pytorch.sh
chmod +x ./torch2trt_onnx.sh && ./torch2trt_onnx.sh
sudo -H python3 -m pip install inputs Adafruit_MotorHat
```

## Install Dependency <a name="install"></a>
Install ROS2 dependency.<br/>
```
sudo apt-get update
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

## Add User to Input Group <a name="user"></a>
Run following command and reboot.<br/>
```
sudo gpasswd -a $USER input
```

## Build, Source & Launch Package (Gamepad) <a name="gamepad"></a>
```
cd ~/ANI717_Robotics/robot_ws/
colcon build --symlink-install && source install/setup.bash && ros2 launch robot_app gamepad_launch.py
```

## Build, Source & Launch Package (Self Driving) <a name="self"></a>
```
cd ~/ANI717_Robotics/robot_ws/
colcon build --symlink-install && source install/setup.bash && ros2 launch robot_app autonomous_launch.py
```

## Launch Arguments <a name="arg"></a>
Select Gamepad type from `logitech` or `waveshare` by editing `line 31` of `launch/launch.py` file.<br/>
Or use these names as arguments for `gamepad_type`.<br/>
Default `gamepad_type`:`logitech`<br/> 

## Zip Images for Download <a name="zip"></a>
```
cd ../
zip -r images.zip images
```
