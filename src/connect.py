#!/usr/bin/env python

import rospy, subprocess, threading, time
from subprocess import Popen, PIPE
from geometry_msgs.msg import Twist, Vector3
from collections import deque

class ConnectNode(object):
    '''
    Creating node to run on neato that will attempt to connect to another free neato to begin with

    Launch neato with 'ROS_NAMESPACE=r1 roslaunch neato_node bringup_minimal.launch host:=192.168.16.82' (the driver in this case has been edited to disable UDP), 
    then this node with 'ROS_NAMESPACE=r1 rosrun virus connect.py'
    '''
    def __init__(self):
        rospy.init_node('connect_node')
        self.launched_nodes = 1
        self.running_nodes = 1
        self.pub_str = '/r1'
        self.pubs = [rospy.Publisher('{}/cmd_vel'.format(self.pub_str), Twist, queue_size=10)]
        self.connected_ips = {'192.168.16.82'} # this is the ip of the original neato connected to
        self.available_ips = deque()
        self.switch = 1

    def connect(self, ip):
        '''
        Attempt to connect to a neato of the provided ip, calls roslaunch with an appropriate launch file then prepares a publisher for the newly connected node
        '''
        if ip in self.connected_ips:
            return
        def roslaunch():
            subprocess.call(['roslaunch', 'virus', 'bringup_child.launch', 'host:={}'.format(ip), 'namespace:=r{}'.format(self.launched_nodes)])

        new_thread = threading.Thread(target=roslaunch)

        self.launched_nodes += 1
        new_thread.start()
        self.pubs.append(rospy.Publisher('{}/r{}/cmd_vel'.format(self.pub_str, self.launched_nodes), Twist, queue_size=10))
        self.connected_ips.add(ip)
        time.sleep(3)

    def search_ips(self):
        '''
        Scans current network for responsive ips, and adds any potentially viable ones to the store of available ips
        '''
        def test_ip(ip):
            pinging = Popen(['ping', '-c', '3', ip], stdout=PIPE)
            pinging.communicate()
            if pinging.returncode == 0:
                rospy.loginfo('Potential ip found: {}'.format(ip))
                self.available_ips.append(ip)
        for i in range(100):
            ip = '192.168.16.{}'.format(i)
            new_thread = threading.Thread(target=test_ip, args=[ip])
            new_thread.start()

    def publish_movement(self, pub):
        '''
        General function for publishing movements to the robots
        '''
        pub.publish(Twist(Vector3(0, 0, 0), Vector3(0, 0, .5 * self.switch)))

    def run(self):
        # self.connect(ip='192.168.16.85')
        self.search_ips()
        while not rospy.is_shutdown():
            if len(self.available_ips):
                self.connect(ip=self.available_ips.popleft())
            # rospy.loginfo('test: {}/r{}/cmd_vel'.format(self.pub_str, self.launched_nodes))
            for pub in self.pubs:
                self.publish_movement(pub)
            self.switch *= -1
            time.sleep(2)


if __name__ == '__main__':
    ConnectNode().run()