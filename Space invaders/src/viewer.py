#!/usr/bin/env python
# license removed for brevity
import rospy
import numpy as np
import gym
#check world debug
import sys
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage
from geometry_msgs.msg import Twist
import pygame
from pygame.locals import *
import cv2
from time import sleep
from random import randint, uniform,random
from world import val,val1
import Recupera as cr


count = -1
lista=[]
video_size = 700, 500
velocity_publisher = rospy.Publisher('space_invader/move', String, queue_size=10)
recuperar=cr.recupera()
data_file=recuperar.lee()
"""
def lectura():
  
  archivo1 = open("/home/flofflye64/Workspace_Station/ROS/catkin_ws/src/ia_lab2/src/dataGathering/datos1.txt", "r")
  #archivo2 = open("/home/flofflye64/Workspace_Station/ROS/catkin_ws/src/ia_lab2/src/dataGathering/datos.txt", "r")
  for linea in archivo1.readlines():
    
    if float(linea) >= 20.0:
      lista=linea
      print(len(lista))
      print(lista)
  archivo1.close()
"""
"""
def movimiento():
    al=0
    al=randint(1,5)
    #print(" Aleatorio:{}".format(al))
    #archivo=open("/home/flofflye64/Workspace_Station/ROS/catkin_ws/src/ia_lab2/src/dataGathering/datos.txt", "a")
    #archivo.write(str(al) + "\n")
    #archivo.close()
    #lectura()
    return al
"""
def key_action():
  #f = open('archivo', 'w')
  #contenido = f.read()
  
  try:
      if data_file != []:
        mov=int(data_file.pop(0))
        print(len(data_file))
        if len(data_file) == 0:
          readFile = open("/home/flofflye64/Workspace_Station/ROS/catkin_ws/src/dataGathering/datos3.txt",'r')
          lines = readFile.readlines()
          readFile.close()
      
          w = open("/home/flofflye64/Workspace_Station/ROS/catkin_ws/src/ia_lab2/src/dataGathering/datos3.txt",'w')
          w.writelines([item for item in lines[:-1]])
          w.write("0")
          w.close()
          
          readFile = open("/home/flofflye64/Workspace_Station/ROS/catkin_ws/src/ia_lab2/src/dataGathering/datos4.txt",'r')
          lines = readFile.readlines()
          readFile.close()
      
          w = open("/home/flofflye64/Workspace_Station/ROS/catkin_ws/src/ia_lab2/src/dataGathering/datos4.txt",'w')
          w.writelines([item for item in lines[:-1]])
          w.close()
        
        print("Archivo",mov)
        if mov == 1:
          return "1"
        if mov == 2:
          return "2"
        if mov == 5:
          return "5"
        if mov == 0:
          return "0"
    
      else:
        global count
        global lista
        mov=0
        keys=pygame.key.get_pressed()
        if keys[K_LEFT]:
          mov= 5
        if keys[K_UP]:
          mov= 1
        if keys[K_RIGHT]:
          mov= 2
        #mov = movimiento()
        count = count + 1
        lista.append(mov)
    
        print(count,val())
        if count == int(val()) and int(val()) > 0:
          print("Iteracion",count)
          with open("/home/flofflye64/Workspace_Station/ROS/catkin_ws/src/ia_lab2/src/dataGathering/datos2.txt", "a") as datos2:
            #datos2.writelines(string=" ".join(str(lista)))
            datos2.writelines("\n".join(map(str,lista)))
      
          readFile = open("/home/flofflye64/Workspace_Station/ROS/catkin_ws/src/ia_lab2/src/dataGathering/datos3.txt",'r')
          lines = readFile.readlines()
          readFile.close()
      
          w = open("/home/flofflye64/Workspace_Station/ROS/catkin_ws/src/ia_lab2/src/dataGathering/datos3.txt",'w')
          w.writelines([item for item in lines[:-1]])
          w.write("0")
          w.close()
          count=0
  
    
        if val1() == "True":
          lista=[]
          readFile = open("/home/flofflye64/Workspace_Station/ROS/catkin_ws/src/ia_lab2/src/dataGathering/datos4.txt",'r')
          lines = readFile.readlines()
          readFile.close()
      
          print("True",lista)
      
          w = open("/home/flofflye64/Workspace_Station/ROS/catkin_ws/src/ia_lab2/src/dataGathering/datos4.txt",'w')
          w.writelines([item for item in lines[:-1]])
          w.close()
          count=0
    
          #keys=pygame.key.get_pressed()
          #vel_msg = Twist()
        print(" Aleatorio:{}".format(mov))
  
        if mov == 5:
          return "5"
        if mov == 1:
          return "1"
        if mov == 2:
          return "2"
        if mov == 0:
          return "0"
  
  except Exception:
    print("No funca")
  #return "0"
  
    

def callback(ros_data):
    np_arr = np.fromstring(ros_data.data, np.uint8)
    image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    screen = pygame.display.set_mode(video_size)
    surf = pygame.surfarray.make_surface(image_np)
    screen.blit(surf, (0, 0))
    pygame.display.update()
    vel_msg = key_action()
    velocity_publisher.publish(vel_msg)

def main(args):
    '''Initializes and cleanup ros node'''
    rospy.init_node('agent', anonymous=True)
    subscriber = rospy.Subscriber('space_invader/image_raw', CompressedImage, callback)
    try:
        screen = pygame.display.set_mode(video_size)
        vel_msg = key_action()
        velocity_publisher.publish(vel_msg)
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down ROS Gym Image Viewer module")
      #cv2.repeat()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
