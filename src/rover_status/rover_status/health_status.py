import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray

class Reciever_node(Node):
    def __init__(self):
        super().__init__("reciever_node")
        self.receive_sub=self.create_subscription(Float32MultiArray,"/rover/batter_temp",self.take_data,10)
        self.get_logger().info("starting too receive the data")
        self.health_status_pub=self.create_publisher(String,"/health_status",10)
       
    def take_data(self, msg: Float32MultiArray):
        self.get_logger().info(f"the data is {msg}")
        self.health_status(msg.data[0])   #getting the battery data and calling the check function 

    def health_status(self,data):   #this would check the battery status and appropriately label warning
        msg=String()
        if int(data) <10:
            msg.data= "CRITICAL"
            self.health_status_pub.publish(msg)
        elif int(data) in range(11,50):
            msg.data= "WARNING"
            self.health_status_pub.publish(msg)
        elif int(data) in range(50,101):
            msg.data= "HEALTHY"
            self.health_status_pub.publish(msg)
        
        
    


def main(args=None):
    rclpy.init(args=args)
    node=Reciever_node()
    rclpy.spin(node)
    rclpy.shutdown()
