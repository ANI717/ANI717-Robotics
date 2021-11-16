<p align="center">
  <h1 align="center">ROS 2 World Simulation</h1>
</p>

<p align="justify">
ROS 2 Package to Simulate a World File in Gazebo Simulation.<br/>
</p>


## Colaborators
[Animesh Bala Ani](https://www.linkedin.com/in/ani717/)


## Table of Contents
* [Install Dependency](#install) <br/>
* [Build, Source & Launch Package](#launch) <br/>
* [Launch Arguments](#arg) <br/>


## Install Dependency <a name="install"></a>
Install ROS2 dependency.<br/>
```
sudo apt-get update
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```


## Build, Source & Launch Package <a name="launch"></a>
```
colcon build --symlink-install --packages-select ros2_world_simulation
source install/local_setup.bash
ros2 launch ros2_world_simulation launch.py
```
```
colcon build --symlink-install && source install/local_setup.bash && ros2 launch ros2_world_simulation launch.py
```


## Launch Arguments <a name="arg"></a>
Select Gamepad type from `logitech` or `waveshare` by editing `line 31` of `launch/launch.py` file.<br/>
Or use these names as arguments for `gamepad_type`.<br/>
Default `gamepad_type`:`logitech`<br/> 
