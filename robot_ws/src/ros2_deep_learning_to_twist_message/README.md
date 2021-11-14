<p align="center">
  <h1 align="center">ROS 2 Deep Learning Package for Robot Movement</h1>
</p>

ROS 2 Package to Publish Twist Message Predicted from Deep Learning Models for Robot Movement.<br/>

## Colaborators
[Animesh Bala Ani](https://www.linkedin.com/in/ani717/)

## Table of Contents
* [Install Dependency](#install) <br/>
* [Build, Source & Launch Package](#launch) <br/>
* [Launch Arguments](#arg) <br/>
* [Settings](#set) <br/>

## Install Dependency <a name="install"></a>
Install `Albumentations`, `Opencv` and `ONNX Runtime`.<br/>
```
sudo -H python3 -m pip install albumentations opencv-python onnxruntime
```
Install ROS2 dependency.<br/>
```
sudo apt-get update
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

## Build, Source & Launch Package <a name="launch"></a>
```
colcon build --symlink-install --packages-select ros2_deep_learning_to_twist_message
source install/local_setup.bash
ros2 launch ros2_deep_learning_to_twist_message launch.py
```
```
colcon build --symlink-install && source install/local_setup.bash && ros2 launch ros2_deep_learning_to_twist_message launch.py
```

## Launch Arguments <a name="arg"></a>
Select Deep Learning Model type by editing `line 39` of `launch/launch.py` file.<br/>
Or use these names as arguments for `model_type`.<br/>
Default `model_type`:`onnx`<br/> 

## Settings <a name="set"></a>
Edit `settings.json` file to assign `xmodel`, `zmodel`, `model_input_shape`, `image topic`, `twist_topic` and `publish frequency`.<br/>
Default `model_input_shape`:`[1, 3, 75, 75]` Input shape of ONNX model<br/>
Default `zmodel`:`z.onnx` ONNX model file to predict `angular z` value<br/>
Default `xmodel`:`x.onnx` ONNX model file to predict `linear z` value<br/>
Default `image topic`:`\image`<br/>
Default `twist topic`:`\cmd_vel`<br/> 
Default `publish frequency`:`100`<br/>
