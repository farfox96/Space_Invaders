#!/usr/bin/env python
# license removed for brevity
import rospy
import gym
import cv2
import numpy as np
import imutils
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage

#check world debug
env = gym.make('SpaceInvaders-v0')
image_pub = rospy.Publisher('space_invader/image_raw', CompressedImage, queue_size=10)

#====================================================================================================================
#from Recuperador import Datos
count=0
itera=0


def pub_image(env):
    #GYM RENDER AS IMAGE
    img = env.render(mode='rgb_array')
    #print(img)
    # ROTATE THE IMAGE THE MATRIX IS 90 grates and mirror
    img = np.flipud(np.rot90(img))
    image_np = imutils.resize(img, width=500)
    # Publish new image
    msg = CompressedImage()
    msg.header.stamp = rospy.Time.now()
    msg.format = "jpeg"
    compressed_images = cv2.imencode('.jpg', image_np)
    msg.data = np.array(compressed_images[1]).tostring()
    image_pub.publish(msg)

def open_world(vel_msg):
    global count
    global itera
    action = int(vel_msg.data)
    obs, rew, done, info = env.step(action)
    pub_image(env)
    count = count + rew
    print(rew, info, done)
    itera = itera + 1
    
    if done == True:
      if int(count) >= 100:
        corte3=open("/home/flofflye64/Workspace_Station/ROS/catkin_ws/src/ia_lab2/src/dataGathering/datos3.txt", "a")
        corte3.write(str(itera))
        corte3.close()
        print(count,itera)
        count=0
        itera=0
      corte2=open("/home/flofflye64/Workspace_Station/ROS/catkin_ws/src/ia_lab2/src/dataGathering/datos4.txt", "a")
      corte2.write("True")
      corte2.close()
      count=0
      itera=0
      env.reset()

#Lee  
def val():
  corte = open("/home/flofflye64/Workspace_Station/ROS/catkin_ws/src/ia_lab2/src/dataGathering/datos3.txt", "r")
  lista=corte.readline()
  corte.close()
  return (lista)
  
#Lee  
def val1():
  corte1 = open("/home/flofflye64/Workspace_Station/ROS/catkin_ws/src/ia_lab2/src/dataGathering/datos4.txt", "r")
  lista=corte1.readline()
  corte1.close()
  return (lista)


if __name__ == '__main__':
    rospy.init_node('space_invader_world', anonymous=True)
    try:
        rospy.Subscriber("space_invader/move", String, open_world)
        env.reset()
        pub_image(env)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
