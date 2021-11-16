<p align="center">
  <h1 align="center">ROS 2 Deep Learning Package for Robot Movement</h1>
</p>

<p align="justify">
ROS 2 Package to Publish Gamepad Controller Inputs to Twist Message for Robot Movement.
</p>

## Colaborators
[Animesh Bala Ani](https://www.linkedin.com/in/ani717/)


## Table of Contents
* [Key Mapping](#key) <br/>
* [Demonstration](#demo) <br/>
* [Install Dependency](#install) <br/>
* [Build, Source & Launch Package](#launch) <br/>
* [Launch Arguments](#arg) <br/>
* [Settings](#set) <br/>


## Install Dependency
Install `Getch`.<br/>
```
python3 -m pip install getch
```
Install ROS2 dependency.<br/>
```
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

## Build, Source & Run Package
```
colcon build && . install/setup.bash && ros2 run ros2_keyboard_to_twist_message execute
```
