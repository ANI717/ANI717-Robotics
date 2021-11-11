<p align="center">
  <h1 align="center">ROS 2 Package to Save Anotated Camera Image</h1>
</p>

ROS 2 Package to Save Camera Image Published in ROS2 Topic along with Geometry Twist Message as Annotation.<br/>

## Colaborators
[Animesh Bala Ani](https://www.linkedin.com/in/ani717/)

## Table of Contents
* [Install Dependency](#install) <br/>
* [Add User to Input Group](#user) <br/>
* [Build, Source & Launch Package](#launch) <br/>
* [Miscellaneous](#miscellaneous) <br/>

## Install Dependency <a name="install"></a>
Install `Opencv`.<br/>
```
python3 -m pip install opencv-python
```
Install ROS2 dependency.<br/>
```
sudo apt-get update
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

## Build, Source & Launch Package <a name="launch"></a>
```
colcon build --symlink-install --packages-select ros2_save_camera_image
source install/local_setup.bash
ros2 launch ros2_save_camera_image launch.py
```
```
colcon build --symlink-install && source install/local_setup.bash && ros2 launch ros2_save_camera_image launch.py
```

## Miscellaneous <a name="miscellaneous"></a>
Select `True` by editing `line 38` of `launch/launch.py` file to launch `ros2 cam2image` for collecting image data with camera.<br/>
Or use this names as arguments for `cam2image`.<br/>
Default `cam2image`:`True`<br/> 

Edit `settings.json` file to assign `image topic`, `twist topic` and `data directory`.<br/>
Default `image topic`:`\images`<br/>
Default `twist topic`:`\cmd_vel`<br/> 
Default `data directory`:`..\images`<br/>
