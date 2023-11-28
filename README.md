Based on various Husarion's GitHub reposistories. Bugfixes and fixes mainly to run it without Docker. E.g.
https://github.com/husarion/webots_ros2/tree/master/webots_ros2_husarion



``` bash
git clone -b ros2 https://github.com/husarion/ros_components_description.git
# in case the package will be used within simulation
export HUSARION_ROS_BUILD_TYPE=simulation

# to specify which simulation engine will be used
# for gazebo classic
export SIMULATION_ENGINE=gazebo-classic
# for ignition gazebo
export SIMULATION_ENGINE=ignition-gazebo

rosdep update --rosdistro $ROS_DISTRO
rosdep install -i --from-path src --rosdistro $ROS_DISTRO -y
colcon build
```
