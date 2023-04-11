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
        # Point(x = 36.001, y = -3.39, z = 0.0),
        Point(x = 2.379, y = 11.766, z = 0.0),
        Point(x = -19.834, y = 12.832, z = 0.0),
        Point(x = 8.782, y = 10.285, z = 0.0),
        Point(x = -21.151, y = 6.262, z = 0)
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