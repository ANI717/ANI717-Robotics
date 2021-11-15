<p align="center">
  <h1 align="center">ROS 2 CSI Camera Image Publish Package for Jetson Nano</h1>
</p>

<p align="justify">
ROS 2 Package to Publish CSI Camera Image as <code>sensor_msgs/Image</code> message on <code>Jetson Nano</code>.
</p>

## Colaborators
[Animesh Bala Ani](https://www.linkedin.com/in/ani717/)

## Table of Contents
* [Install Dependency](#install) <br/>
* [Build, Source & Launch Package](#launch) <br/>
* [Launch Arguments](#arg) <br/>
* [Settings](#set) <br/>

## Install Dependency <a name="install"></a>
Install ROS2 dependency.<br/>
```
sudo apt-get update
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

## Build, Source & Launch Package <a name="launch"></a>
```
colcon build --symlink-install --packages-select ros2_csi_camera_publish
source install/local_setup.bash
ros2 launch ros2_csi_camera_publish launch.py
```
```
colcon build --symlink-install && source install/local_setup.bash && ros2 launch ros2_csi_camera_publish launch.py
```

## Settings <a name="set"></a>
Edit `settings.json` file to assign `xmodel`, `zmodel`, `model_input_shape`, `image topic`, `twist_topic` and `publish frequency`.<br/>
Default `model_input_shape`:`[1, 3, 75, 75]` - Input shape of ONNX model<br/>
Default `zmodel`:`z.onnx` - ONNX model file to predict `angular z` value<br/>
Default `xmodel`:`x.onnx` - ONNX model file to predict `linear z` value<br/>
Default `image topic`:`\image`<br/>
Default `twist topic`:`\cmd_vel`<br/> 
Default `publish frequency`:`100`<br/>
