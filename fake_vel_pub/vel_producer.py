import rclpy
import random
from rclpy.node import Node
from geometry_msgs.msg import Twist

class VelPub1(Node):

    def __init__(self):
        super().__init__('vel_pub1')
        self.publisher_ = self.create_publisher(Twist, 'topic_vel', 10)
        self.timer = self.create_timer(3.0, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        vel = Twist()
        vel.linear.x = round(random.uniform(00.00, 100.00), 2)
        vel.linear.y = round(random.uniform(00.00, 100.00), 2)
        vel.linear.z = round(random.uniform(00.00, 100.00), 2)
        vel.angular.x = round(random.uniform(00.00, 100.00), 2)
        vel.angular.y = round(random.uniform(00.00, 100.00), 2)
        vel.angular.z = round(random.uniform(00.00, 100.00), 2)
        self.publisher_.publish(vel)
        self.get_logger().info('\n'+ 'Pub linear velocity'+'\n'+'x: ' + str(vel.linear.x) + 
                               ', y: ' + str(vel.linear.y) + ', z: ' + str(vel.linear.z)
                               +'\n'+ 'Pub angular velocity'+'\n'+'x: ' + str(vel.angular.x) +
                               ', y: ' + str(vel.angular.y) + ', z: ' + str(vel.angular.z))
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    vel_pub1 = VelPub1()
    rclpy.spin(vel_pub1)
    vel_pub1.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()