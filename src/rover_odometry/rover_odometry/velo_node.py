#this is the publisher for the random odometry data from rover every second
import rclpy
from rclpy.node import Node
from custom_msgs.msg import RoverOdometry 
import random
from geometry_msgs.msg import Twist
class OdometryData(Node):
    def __init__(self):
        super().__init__("Odo_Data_Node")
        self.odo_data_pub= self.create_publisher(RoverOdometry,"/odometry_data",10)
        self.create_timer(1.0,self.timer_callback)
    def timer_callback(self):
        msg = RoverOdometry()
        t=Twist()
        t.linear.x=random.uniform(0,5)
        t.linear.y=random.uniform(0,5)
        self.get_logger().info(f"{t.linear.x},{t.linear.y}")
        msg.angular_velocity= random.uniform(0,10)
        msg.linear_velocity=t
        self.odo_data_pub.publish(msg)



def main(args=None):
    rclpy.init(args=args)
    node = OdometryData()
    rclpy.spin(node)

    rclpy.shutdown()