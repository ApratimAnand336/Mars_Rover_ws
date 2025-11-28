import rclpy
from rclpy.node import Node 
from std_msgs.msg import Float32MultiArray 
from std_msgs.msg import String

#this node subscribes both the topics and print whole scenario

class info_receive(Node):
    def __init__(self):
        super().__init__("info_node")
        self.sensor_sub=self.create_subscription(Float32MultiArray,"/rover/batter_temp",self.sensor,10)
        self.health_sub=self.create_subscription(String,"/health_status",self.health,10)
    def sensor(self,msg: Float32MultiArray):
        print(f"the battery level is {int(msg.data[0])} and the temp is {msg.data[1]} degrees")
        
    def health(self,msg: String):
        print(f"and the health status shows {msg.data}")
def main(args=None):
    rclpy.init(args=args)
    node=info_receive()
    rclpy.spin(node)
    

    rclpy.shutdown()