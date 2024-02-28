import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class VelPub3(Node):

    def __init__(self):
        super().__init__('vel_pub3')
        self.subscription = self.create_subscription(Twist, 'topic_vel',
            self.listener_callback1, 10)
        self.subscription = self.create_subscription(Twist, 'topic_vel_double',
            self.listener_callback2, 10)
        self.subscription  # prevent unused variable warning

    def listener_callback1(self, msg):
        self.get_logger().info('\n'+ 'Detect linear velocity:'+'\n'+'x: ' + str(msg.linear.x) + 
                               ', y: ' + str(msg.linear.y) + ', z: ' + str(msg.linear.z)
                               +'\n'+ 'Detect angular velocity'+'\n'+'x: ' + str(msg.angular.x) +
                               ', y: ' + str(msg.angular.y) + ', z: ' + str(msg.angular.z))
    def listener_callback2(self, msg2):
        self.get_logger().info('\n'+ 'Detect double linear velocity'+'\n'+'x: ' + str(msg2.linear.x) + 
                               ', y: ' + str(msg2.linear.y) + ', z: ' + str(msg2.linear.z)
                               +'\n'+ 'Detect double angular velocity'+'\n'+'x: ' + str(msg2.angular.x) +
                               ', y: ' + str(msg2.angular.y) + ', z: ' + str(msg2.angular.z))

def main(args=None):
    rclpy.init(args=args)
    vel_pub3 = VelPub3()
    rclpy.spin(vel_pub3)
    vel_pub3.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()