#!/usr/bin/env python3

# Examples:
# https://github.com/ROBOTIS-GIT/turtlebot3/blob/master/turtlebot3_teleop/nodes/turtlebot3_teleop_key

import rospy
from geometry_msgs.msg import Twist
import time

if __name__=="__main__":
    rospy.init_node('rover_control')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rover_cmd = Twist()
    print(f"pub: {pub}")
    print(f"rover_cmd: \n{rover_cmd}")

    vel_x = 0.5
    yaw = 0.3

    try:
        while not rospy.is_shutdown():
            rover_cmd.linear.x = 0.5
            rover_cmd.linear.y = 0.0
            rover_cmd.linear.z = 0.0

            rover_cmd.angular.x = 0.0
            rover_cmd.angular.y = 0.0
            rover_cmd.angular.z = 0.3

            pub.publish(rover_cmd)

            print(f"Published from rover_control - vel_x: {vel_x} :: yaw: {yaw}")
            time.sleep(1)

    except:
        print(e)

    finally:
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)


