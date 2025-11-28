from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    return LaunchDescription([
        Node(
            package="rover_status",
            executable="sensor_node",
            name="sensor_node",
            output="screen"
        ),
        Node(
            package="rover_status",
            executable="health_node",
            name="reciever_node",
            output="screen"
        ),
        Node(
            package="rover_status",
            executable="info_node",
            name="info_node",
            output="screen"
        )

    ])

    