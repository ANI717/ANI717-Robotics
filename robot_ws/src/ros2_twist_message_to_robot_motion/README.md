<p align="center">
  <h1 align="center">A Generalized ROS 2 Package for Robot Movement</h1>
</p>

A generalized ROS2 package to move `Nvidia Jetbot` or any `Adafruit MotorHat` driven robot. The package subscribes to `/cmd_vel` topic, to acquire steering and speed control instructions in `geometry_msgs/Twist.msg` message format. `linear.x` controls forward-backward movement and  `angular.z` controls steering.


## Colaborators
[Animesh Bala Ani](https://www.linkedin.com/in/ani717/)


## Table of Contents
* [Key Mapping](#key) <br/>
* [Demonstration](#demo) <br/>
* [Install Dependency](#install) <br/>
* [Build, Source & Launch Package](#launch) <br/>
* [Miscellaneous](#miscellaneous) <br/>


## Key Mapping <a name="key"></a>
`+ linear.x` : `Forward`<br/>
`- linear.x` : `Backward`<br/>
`+ angular.z` : `Right`<br/>
`- angular.z` : `Left`<br/>


## Demonstration <a name="demo"></a>
Demonstration of robot movement.<br/>
Direction: `Backward` `Left`.<br/>

<img src="https://github.com/ANI717/ani717_gif_repository/blob/main/ros2_twist_message_to_robot_motion/jetbot_motion.gif" alt="JupytarLab Interface" class="inline"/><br/>


## Install Dependency <a name="install"></a>
Install `traitlets`, `multiexit` and `Adafruit_MotorHat`.
```
sudo -H python3 -m pip install Adafruit_MotorHat traitlets multiexit
```
Install ROS2 dependency.
```
sudo apt-get update
rosdep update
rosdep update && rosdep install --from-paths src --ignore-src -r -y
```


## Build, Source & Run Package <a name="launch"></a>
```
colcon build --symlink-install --packages-select ros2_twist_message_to_robot_motion
source install/local_setup.bash
ros2 launch ros2_twist_message_to_robot_motion launch.py
```
```
colcon build --symlink-install && source install/local_setup.bash && ros2 launch ros2_twist_message_to_robot_motion launch.py
```

## Miscellaneous <a name="miscellaneous"></a>
Select Robot type from `jetbot` or `adafruit` by editing `line 35` of `launch/launch.py` file.<br/>
Or use these names as arguments for `robot_type`.<br/>
Default `robot_type`:`jetbot`<br/> 

Edit `settings.json` file to assign `x_calibration` and `z_calibration`.<br/>
Default `x_calibration`:`0.50`<br/> 
Default `z_calibration`:`0.25`<br/>
