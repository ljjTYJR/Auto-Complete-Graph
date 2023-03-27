#! /usr/bin/env python
import rospy
# import std_msgs.msg
from std_msgs.msg import Header
import time
from geometry_msgs.msg import Point, PointStamped
from std_msgs.msg import Bool

def send_msgs():
    rospy.init_node('basement_alignment_publisher')
    pub = rospy.Publisher('/clicked_point', PointStamped, queue_size=10)
    points = [
        # prior/sensor; prior/sensor
        Point(x = -27.874, y = -7.901, z = 0.0),
        Point(x = -10.143, y = -3.593, z = 0.0),
        Point(x = -27.094, y = 7.010, z = 0.0),
        Point(x = -9.777, y = 1.790, z = 0)
    ]
    for n in range(4):
        time.sleep(0.5)
        p = points[n]
        # h.stamp = rospy.Time.now()
        print("Sending clicked point command at point:", p)
        pub.publish(PointStamped(point = p,header = Header(stamp=rospy.Time.now(), frame_id='odom')))

    pub2 = rospy.Publisher('/publish_occ_acg', Bool, queue_size=10)
    z = Bool()
    z.data = True
    time.sleep(0.5)
    pub2.publish(z)
    print("Sending publish occ acg command")


if __name__ == "__main__":
    send_msgs()