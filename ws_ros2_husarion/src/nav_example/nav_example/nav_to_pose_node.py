#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose

class NavToPoseNode(Node):
    def __init__(self):
        super().__init__('nav_to_pose_node')
        self._action_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        self.get_logger().info('NavToPoseNode has been started.')

    def send_goal(self, x, y, theta=0.0):
        self.get_logger().info('Waiting for action server...')
        self._action_client.wait_for_server()

        goal_msg = NavigateToPose.Goal()

        # Set up the target pose
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.pose.position.x = float(x)
        pose.pose.position.y = float(y)
        pose.pose.position.z = 0.0
        
        # very simple orientation, assuming moving in +x direction or staying roughly 0 rad yaw
        pose.pose.orientation.x = 0.0
        pose.pose.orientation.y = 0.0
        pose.pose.orientation.z = 0.0
        pose.pose.orientation.w = 1.0

        goal_msg.pose = pose

        self.get_logger().info(f'Sending goal request: x={x}, y={y}...')
        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f'Distance remaining: {feedback.distance_remaining:.2f} meters')

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            rclpy.shutdown()
            return

        self.get_logger().info('Goal accepted :)')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        status = future.result().status
        
        # 4 corresponds to SUCCEEDED
        if status == 4:
            self.get_logger().info('Goal succeeded!')
        else:
            self.get_logger().info(f'Goal failed with status code: {status}')

        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    action_client = NavToPoseNode()
    
    # Send a goal to exactly x=1.0, y=1.0
    action_client.send_goal(1.0, 1.0)
    
    rclpy.spin(action_client)

if __name__ == '__main__':
    main()
