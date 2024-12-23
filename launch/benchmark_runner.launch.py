import os
from os.path import join as joinPath

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    dataset_path_launch_arg = DeclareLaunchArgument(
        "bag_file",
        default_value=joinPath(os.environ["HOME"], "bag_perception_benchmark", "sample.bag"),
        description="rosbag file to replay (.db3)",
    )

    use_camera_launch_arg = DeclareLaunchArgument(
        "use_camera",
        default_value="False",
        description="",
    )

    result_path_launch_arg = DeclareLaunchArgument(
        "result_path",
        default_value=joinPath(os.environ["HOME"], "benchmark_result"),
        description="",
    )

    # benchmark_frame_launch_arg = DeclareLaunchArgument("benchmark_frame", default_value="base_link")

    launch_file_launch_arg = DeclareLaunchArgument(
        "launch_file",
        default_value="benchmark_perception.launch.xml",
        description="Launch file for testing perception stack",
    )

    vehicle_model_launch_arg = DeclareLaunchArgument(
        "vehicle_model",
        default_value="awsim_labs_vehicle",
        description="",
    )

    sensor_model_launch_arg = DeclareLaunchArgument(
        "sensor_model",
        default_value="awsim_labs_sensor_kit",
        description="",
    )

    # benchmark_node = Node(
    #     package="perception_benchmark_tool",
    #     name="benchmark_node",
    #     executable="benchmark_node",
    #     output="screen",
    #     parameters=[
    #         {
    #             "result_path": LaunchConfiguration("result_path"),
    #             "benchmark_frame": LaunchConfiguration("benchmark_frame"),
    #         }
    #     ],
    # )

    bag_player_node = Node(
        package="bag_perception_benchmark",
        name="bag_player_node",
        executable="bag_player_node",
        output="screen",
        parameters=[
            {
                "bag_file": LaunchConfiguration("bag_file"),
                "sensor_model": LaunchConfiguration("sensor_model"),
            }
        ],
    )

    autoware_workflow_runner_node = Node(
        package="bag_perception_benchmark",
        name="autoware_workflow_runner_node",
        executable="autoware_workflow_runner_node",
        output="screen",
        parameters=[
            {
                "launch_file": LaunchConfiguration("launch_file"),
                "vehicle_model": LaunchConfiguration("vehicle_model"),
                "sensor_model": LaunchConfiguration("sensor_model"),
            }
        ],
    )

    return LaunchDescription(
        [
            dataset_path_launch_arg,
            use_camera_launch_arg,
            # benchmark_frame_launch_arg,
            result_path_launch_arg,
            launch_file_launch_arg,
            vehicle_model_launch_arg,
            sensor_model_launch_arg,
            # benchmark_node,
            bag_player_node,
            autoware_workflow_runner_node,
        ]
    )
