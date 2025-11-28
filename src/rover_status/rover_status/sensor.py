import rclpy
from rclpy.node import Node
import random
from std_msgs.msg import Float32MultiArray

class SensorNode(Node):
    def __init__(self):
        super().__init__("sensor_node")   #this is the  real name of the node 
        
        self.get_logger().info("the sensor data is started ") #logger to know if node has started
        self.battery_temp_pub=self.create_publisher(Float32MultiArray,"/rover/batter_temp",10)
        self.create_timer(5.0,self.timer_callback)
    def timer_callback(self):
        self.BATTERY_data= random.uniform(0,100)
        self.temp=random.uniform(-20,80)
        
        msg=Float32MultiArray()
        msg.data=[self.BATTERY_data,self.temp]
        self.battery_temp_pub.publish(msg)

        
        

        

def main(args=None):
    rclpy.init(args=args)

    node=SensorNode()
    rclpy.spin(node)   
    rclpy.shutdown()

