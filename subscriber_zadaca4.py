import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            '/broj',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.publisher_ = self.create_publisher(Int32, '/kvadrat_broja', 10)

    def listener_callback(self, msg):
        kvadrat = msg.data ** 2
        self.get_logger().info('Received: %d, Kvadrirano: %d' % (msg.data, kvadrat))
        kvadrat_msg = Int32()
        kvadrat_msg.data = kvadrat
        self.publisher_.publish(kvadrat_msg)

def main(args=None):
    rclpy.init(args=args) 

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
