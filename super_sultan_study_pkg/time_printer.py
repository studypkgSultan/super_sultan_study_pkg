#!/usr/bin/env python3
"""Узел, который каждые 5 секунд выводит текущее время"""

import rclpy
from rclpy.node import Node
from datetime import datetime

class TimePrinter(Node):
    def __init__(self):
        super().__init__('time_printer')
        # Создаём таймер на 5 секунд
        self.timer = self.create_timer(5.0, self.timer_callback)
        self.get_logger().info("Time Printer node started!")

    def timer_callback(self):
        # Получаем текущее время
        current_time = datetime.now().strftime("%H:%M:%S")
        self.get_logger().info(f"Current time: {current_time}")

def main(args=None):
    rclpy.init(args=args)
    node = TimePrinter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
