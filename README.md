# Robot Operating System
ROS version Noetic

![commonMD](mobile_robot/ros_gazebo_test02.png)

# Workspace
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

# URDF
mkdir urdf

roscd mobile_robot

touch rover.urdf

cd ~/test_ws

code .

# RViz And Gazebo
'''
cd ~/catkin_ws/src/mobile_robot
'''
'''
mkdir launch
'''
'''
cd launch
'''
'''
touch rviz.launch
'''
'''
touch gazebo.launch
'''
'''
roslaunch mobile_robot rviz.launch
'''
'''
roslaunch mobile_robot gazebo.launch
'''

# Keyboard Teleoperations
'''
sudo apt update
'''
'''
sudo apt install ros-noetic-teleop-twist-keyboard
'''
'''
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
'''

# Topics And Nodes Works
rqt / Plugins / Message Publisher

rqt / Plugins / Robot Tools / Robot Steering
'''
rosnode list
'''
'''
rostopic list
'''
'''
rostopic pub /cmd_vel
'''
'''
rostopic echo /cmd_vel
'''
'''
rostopic echo /odom
'''

# Python Scripts
'''
cd ~/catkin_ws/src/mobile_robot/src
'''
'''
touch test_publisher.py
'''
'''
rosrun mobile_robot test_publisher.py
'''



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

# Linux Console 
### Disable Auto Logout Screen
'''
xfce4-screensaver-preferences
'''
![commonMD](mobile_robot/xubuntu_lockscreen_off.png)
### Colors In Console
Consoles tty1, tty2, ..., tty6
Ctrl + F1, Ctrl + F2, ..., 
'''
setterm --background white --foreground black --store
'''
Ctrl + L - clear console.
### Colors In Terminal Emulator Of Xubuntu
![commonMD](mobile_robot/xubuntu_colors_terminal.png)

# Images for GitFlic

![commonMD](mobile_robot/ros_extension_settings.png)

![commonMD](mobile_robot/ros_urdf_preview01.png)

![commonMD](mobile_robot/ros_urdf_preview02.png)

![commonMD](mobile_robot/ros_rviz_test01.png)

![commonMD](mobile_robot/ros_rviz_test02.png)

![commonMD](mobile_robot/ros_rviz_test03.png)

![commonMD](mobile_robot/ros_rviz_test04.png)

![commonMD](mobile_robot/ros_gazebo_test01.png)

![commonMD](mobile_robot/ros_gazebo_test02.png)
