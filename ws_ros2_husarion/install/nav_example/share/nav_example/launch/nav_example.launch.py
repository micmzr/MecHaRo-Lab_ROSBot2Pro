import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    nav_to_pose_node = Node(
        package='nav_example',
        executable='nav_to_pose_node',
        name='nav_to_pose_node',
        output='screen'
    )

    return LaunchDescription([
        nav_to_pose_node
    ])
