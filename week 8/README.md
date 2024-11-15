$ source /opt/galactic/setup.bash
$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
$ ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True
$ ros2 run turtlebot3_teleop teleop_keyboard

link video tutorial https://www.youtube.com/watch?v=OcifO_xJBe0
