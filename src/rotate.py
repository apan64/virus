#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, Vector3

class RotateNode(object):
    '''
    Creating simple rotate node to ensure connection works
    '''
    def __init__(self):
        rospy.init_node('rotate_node')
        self.vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    def run(self):
        while not rospy.is_shutdown():
            self.vel_pub.publish(Twist(Vector3(0, 0, 0), Vector3(0, 0, 1)))

if __name__ == '__main__':
    RotateNode().run()
