Based on various Husarion's GitHub reposistories. Bugfixes and fixes mainly to run it without Docker. E.g.
- https://github.com/husarion/webots_ros2/tree/master/webots_ros2_husarion
- https://github.com/husarion/rosbot_ros
- https://github.com/husarion/rosbot-mapping
- https://github.com/husarion/rosbot-navigation

**PC**

Everything presented here is mean to be run on the PC. Though navigation may work better if it would run directly on the robot due to network issues.

_Install_

``` bash
git clone -b humble https://github.com/micmzr/MecHaRo-Lab_ROSBot2Pro.git
cd MecHaRo-Lab_ROSBot2Pro/ws_ros2_husarion
rosdep install --ignore-src --from-path src/ -y --rosdistro $ROS_DISTRO
colcon build
source install/setup.bash
```

**_Simulation_**

Generally each command should be run in separate terminal tab. Please remember to run source command. 

_RViz_
``` bash
ros2 run rviz2 rviz2 -d ./src/rosbot_ros/rosbot_description/settings/rosbot2-nav2-demo.rviz
```
_Webots_
``` bash
ros2 launch webots_ros2_husarion rosbot_launch.py
```

To create map: 

_Mapping_ 
``` bash
ros2 launch slam_toolbox online_sync_launch.py slam_params_file:=./src/rosbot_ros/rosbot_description/settings/slam_toolbox_webots.yaml use_sim_time:='True'
```
_Keyboard control_
``` bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
_Map saver_
``` bash
while true; do ros2 run nav2_map_server map_saver_cli --free 0.15 --fmt png -f ./maps/map; sleep 5; done
```

To run navigation:

_Localization_
``` bash
ros2 launch nav2_bringup localization_launch.py params_file:=./src/rosbot_ros/rosbot_description/settings/amcl_params.yaml map:=./maps/map.yaml use_sim_time:='True'
```
_Navigation_
``` bash
ros2 launch nav2_bringup navigation_launch.py params_file:=./src/rosbot_ros/rosbot_description/settings/nav2_params.yaml use_sim_time:='True'
```

**_Real robot_**

The robot should be switched on and all ROS2 nodes should run on it correctly.

_RViz_
``` bash
ros2 run rviz2 rviz2 -d ./src/rosbot_ros/rosbot_description/settings/rosbot2-nav2-demo.rviz
```

To create map: 

_Mapping_ 
``` bash
ros2 launch slam_toolbox online_sync_launch.py slam_params_file:=./src/rosbot_ros/rosbot_description/settings/slam_toolbox.yaml use_sim_time:='False' 
```
_Keyboard controll_
``` bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
_Map saver_
``` bash
while true; do ros2 run nav2_map_server map_saver_cli --free 0.15 --fmt png -f ./maps/map; sleep 5; done
```

To run navigation:

_Localization_
``` bash
ros2 launch nav2_bringup localization_launch.py params_file:=./src/rosbot_ros/rosbot_description/settings/amcl_params.yaml map:=./maps/map.yaml use_sim_time:='False'
```
_Navigation_
``` bash
ros2 launch nav2_bringup navigation_launch.py params_file:=./src/rosbot_ros/rosbot_description/settings/nav2_params.yaml use_sim_time:='False'
```
