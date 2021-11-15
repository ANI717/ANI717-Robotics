## Install Required Packages (Jetson Nano)
Install `ROS2 Dashing`, `PyTorch`, `Torchvision`, `ONNXRuntime-GPU`, `Inputs` and `Adafruit_MotorHat`.<br/>
```
git clone https://github.com/ANI717/Headless-Jetson-Nano-Setup
cd ~/Headless-Jetson-Nano-Setup
chmod +x ./dashing.sh && ./dashing.sh
chmod +x ./pytorch.sh && ./pytorch.sh
chmod +x ./torch2trt_onnx.sh && ./torch2trt_onnx.sh
sudo -H python3 -m pip install inputs Adafruit_MotorHat
```

## Install Dependency
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

## Build, Source & Launch Package (Gamepad)
```
cd ~/ANI717_Robotics/robot_ws/
colcon build --symlink-install && source install/setup.bash && ros2 launch robot_app gamepad_launch.py
```

## Build, Source & Launch Package (Self Driving)
```
cd ~/ANI717_Robotics/robot_ws/
colcon build --symlink-install && source install/setup.bash && ros2 launch robot_app autonomous_launch.py
```

## Zip Images for Download
```
cd ../
zip -r images.zip images
```
