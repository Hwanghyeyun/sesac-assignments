#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from interfaces.msg import ObjectsInfo  

class Subscriber(Node):
    def __init__(self):
           super().__init__('subscriber')
           self.subscription = self.create_subscription(
               ObjectsInfo,
               '/yolov5_ros2/object_detect',
               self.listener_callback,
               10 )
        # TODO: Implement node initialization
        # TODO: Register callback
        

    def listener_callback(self, msg):
          # TODO: Implemnt a callback
        if len(msg.objects) == 0:
            self.get_logger().info("감지된 객체 없음")
        else:
            for obj in msg.objects:
                box_str = ','.join(str(v) for v in obj.box)  # [x1, y1, x2, y2]
                self.get_logger().info(
                    f"[감지됨] class={obj.class_name}, "
                    f"score={obj.score:.2f}, "
                    f"box=[{box_str}], "
                    f"img_size=({obj.width}x{obj.height})"
                )
       


def main(args=None):
    rclpy.init(args=args)
    node = Subscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
