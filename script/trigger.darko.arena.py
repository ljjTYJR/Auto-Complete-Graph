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
        # prior/sensor; prior/sensor (rosbag:left)
        # "arena_vertical_flip.png"
        # Point(x = -13.161, y = 57.8, z = 0.0),
        # Point(x = -4.151, y = 3.272, z = 0.0),
        # Point(x = 3.011, y = 57.13, z = 0.0),
        # Point(x = 20.25, y = 6.024, z = 0)

        # prior/sensor; prior/sensor (rosbag:fullmap)
        # Point(x = 2.929, y = 57.084, z = 0.0),
        # Point(x = 21.893, y = 2.633, z = 0.0),
        # Point(x = -13.099, y = 57.743, z = 0.0),
        # Point(x = -2.330, y = 3.747, z = 0)

        # 20230525-2.png
        # Point(x = 103.511,  y = 250.840,    z = 0.0),
        # Point(x = 19.902,   y = 6.027,      z = 0.0),
        # Point(x = 67.937,   y = 254.412,    z = 0.0),
        # Point(x = -4.091,   y = 3.327,      z = 0.0)

        # 20230526.png
        # Point(x = -0.293,  y = 66.775,    z = 0.0),
        # Point(x = 20.233,   y = 5.925,      z = 0.0),
        # Point(x = -14.043,   y = 60.167,    z = 0.0),
        # Point(x = -4.205,   y = 3.524,      z = 0.0)

        # 20230526-2.png
        # Point(x = 0.343,  y = 67.345,    z = 0.0),
        # Point(x = 19.978,   y = 6.054,      z = 0.0),
        # Point(x = -14.214,   y = 60.321,    z = 0.0),
        # Point(x = -4.397,   y = 3.227,      z = 0.0)

        # 20230526-3_thinner.png
        Point(x = -0.233,  y = 67.080,    z = 0.0),
        Point(x = 20.165,   y = 5.935,      z = 0.0),
        Point(x = -14.654,   y = 59.749,    z = 0.0),
        Point(x = -4.205,   y = 3.436,      z = 0.0)
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