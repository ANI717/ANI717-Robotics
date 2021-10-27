<p align="center">
  <h1 align="center">ROS 2 Package to Save Anootated Camera Image</h1>
</p>

ROS 2 Package to Save Camera Image Published in ROS2 Topic along with Geometry Twist Message as Annotation.<br/>

## Install Dependency
Install ROS2 dependency.<br/>
```
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

## Build, Source & Run Package
```
colcon build && . install/setup.bash && ros2 run ros2-save-camera-image execute
```

## Launch Package
```
colcon build && . install/setup.bash && ros2 launch ros2-save-camera-image launch.py
```
