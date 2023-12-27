# Robot Operating System
ROS version Noetic

#Workspace
mkdir -p ~/test_ws/src

cd ~/test_ws/src

catkin_init_workspace

cd ~/test_ws

catkin_make

source devel/setup.bash

roscd - check ws

# Package
cd ~/test_ws/src

catkin_create_pkg mobile_robot std_msgs rospy urdf 
                xacro rviz gazebo tf2 
                geometry_msgs 
                joint_state_publisher_gui

cd ~/test_ws

catkin_make --only-pkg-with-deps mobile_robot

source devel/setup.bush

roscd mobile_robot

#URDF
mkdir urdf

mkdir launch

roscd mobile_robot

touch rover.urdf

cd ~/test_ws

code .

# Visual Studio Code

Ctrl + Shift + P

run Extension VS Code

ROS Preview URDF

ROS Microsoft Pre-release

URDF smilerobotics urdf/xacro snippets

ROS Snippets Liews Wuttipat

Ctrl + ], [ - Indent

Ctrl + / - comment line

# Introspection
printenv | grep ROS

roscd

<img src="mobile_robot/ros_extension_settings.png">

<img src="mobile_robot/ros_urdf_preview01.png">

<img src="mobile_robot/ros_urdf_preview02.png">

<img src="mobile_robot/ros_rviz_test01.png">

<img src="mobile_robot/ros_rviz_test02.png">

<img src="mobile_robot/ros_rviz_test03.png">

<img src="mobile_robot/ros_rviz_test04.png">

<img src="mobile_robot/ros_gazebo_test01.png">

<img src="mobile_robot/ros_gazebo_test02.png">

