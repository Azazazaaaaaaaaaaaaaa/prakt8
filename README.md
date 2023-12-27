ROS version Noetic
Robot Operating System

Cheat sheet

Workspace

mkdir -p ~/test_ws/src
cd ~/test_ws/src
catkin_init_workspace
cd ~/test_ws
catkin_make
source devel/setup.bash

cd ~/test_ws/src
catkin_create_pkg mobile_robot std_msgs rospy urdf 
                  xacro rviz gazebo tf2 
                  geometry_msgs 
                  joint_state_publisher_gui

cd ~/test_ws
catkin_make
source devel/setup.bush

roscd mobile_robot
mkdir urdf
mkdir launch
roscd mobile_robot
touch rover.urdf

cd ~/test_ws
code .

catkin_make --pkg=mobile_robot


Visual Studio Code
Ctrl + Shift + P
run Extension VS Code
ROS Preview URDF
ROS Microsoft Pre-release
URDF Smilerobot snippets


printenv | grep ROS
roscd

<img src="mobile_robot/ros_extension_settings.png">

<img src="mobile_robot/ros_urdf_preview01.png">
