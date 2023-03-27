# send a string message to /test

import rospy
from std_msgs.msg import String
import time
from std_msgs.msg import Bool

if __name__ == "__main__":
    rospy.init_node('test_publisher')
    pub = rospy.Publisher('/publish_occ_acg', Bool, queue_size=10)
    z = Bool()
    z.data = True
    time.sleep(0.5)
    pub.publish(z)
    print("Sent message")

