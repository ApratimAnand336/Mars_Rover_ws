#this will subs to velocity node published data and update the coord accordingly
#also check the speed limit and give appropriate warnings

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from custom_msgs.msg import RoverOdometry


class coord(Node):
    def __init__(self):
        super().__init__("coord_node")

        
        self.x=0
        self.y=0
        self.oreo=0   #initially at zeero degrees
        self.odo_data_sub=self.create_subscription(RoverOdometry,"/odometry_data",self.data_callback,10)

    def data_callback(self,msg: RoverOdometry):
        x_velo=msg.linear_velocity.linear.x
        y_velo=msg.linear_velocity.linear.y
        ang_velo=msg.angular_velocity

        self.x+= x_velo
        self.y+=y_velo
        self.oreo+=ang_velo
        velo=(x_velo**2+y_velo**2)**(1/2)

        if velo > 3:
            warning="SPEED WARNING!!"
        else:
            warning="ALL GOOD!!!" 
        self.get_logger().info(f"the coordinates are {self.x} and {self.y} with orientation {self.oreo} and {warning} for velocity {velo}")
        # self.get_logger().info(f"{msg.linear_velocity.linear.x},{msg.linear_velocity.linear.y}")




def main(args=None):
    rclpy.init(args=args)
    node=coord()
    rclpy.spin(node)
    rclpy.shutdown()