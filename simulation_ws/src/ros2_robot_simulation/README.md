<p align="center">
  <h1 align="center">ROS 2 Robot Simulation</h1>
</p>

<p align="justify">
ROS 2 Package to Simulate a Robot in Gazebo Simulation. One can put any <code>*Robot URDF</code> file in <code>models/urf</code> folder and related <code>mesh</code> files in <code>models/meshes</code> folder. Change <code>line 97</code> in <code>launch/launch.py</code> to select the urdf file of robot. Default is <code>jetbot.xml</code>.
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
export DISPLAY=:0
colcon build --symlink-install --packages-select ros2_robot_simulation
source install/local_setup.bash
ros2 launch ros2_robot_simulation launch.py
```
```
colcon build --symlink-install && source install/local_setup.bash && ros2 launch ros2_robot_simulation launch.py
```


## Launch Arguments <a name="arg"></a>
Select `True` or `False` as arguments for `use_simulator` to decide whether to launch `gazebo server`.<br/>
Default `use_simulator`:`True`<br/>

Select `True` or `False` as arguments for `headless` to decide whether to launch `gazebo client`.<br/>
Default `headless`:`True`<br/>

Select `complete path of world file` as arguments for `world` to simulate that world.<br/>
Default `world`:`os.path.join(package_dir, 'worlds', 'empty.world')`<br/>
