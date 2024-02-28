import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class VelPub2(Node):

    def __init__(self):
        super().__init__('vel_pub2')
        self.subscription = self.create_subscription(Twist, 'topic_vel',
            self.double, 10)
        self.subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(Twist, 'topic_vel_double', 10)

    def double(self, vel):
        vel2 = Twist()
        vel2.linear.x = vel.linear.x * 2
        vel2.linear.y = vel.linear.y * 2
        vel2.linear.z = vel.linear.z * 2
        vel2.angular.x = vel.angular.x * 2
        vel2.angular.y = vel.angular.y * 2
        vel2.angular.z = vel.angular.z * 2
        self.publisher_.publish(vel2)
        self.get_logger().info('\n'+ 'Pub double linear velocity'+'\n'+'x: ' + str(vel2.linear.x) + 
                               ', y: ' + str(vel2.linear.y) + ', z: ' + str(vel2.linear.z)
                               +'\n'+ 'Pub double angular velocity'+'\n'+'x: ' + str(vel2.angular.x) +
                               ', y: ' + str(vel2.angular.y) + ', z: ' + str(vel2.angular.z))

def main(args=None):
    rclpy.init(args=args)
    vel_pub2 = VelPub2()
    rclpy.spin(vel_pub2)
    vel_pub2.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()