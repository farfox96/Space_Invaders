"""
def archi():
  with open("/home/flofflye64/Workspace_Station/ROS/catkin_ws/src/ia_lab2/src/dataGathering/datos2.txt", "r") as datos:
    l1=datos.readlines()
    for x in range(0,len(l1)):
      print(l1[x])
      return (l1[x])
"""
class recupera:
  contador=0
  def __init__(self):
    pass
    
  def lee(self):
    archivo=open("/home/flofflye64/Workspace_Station/ROS/catkin_ws/src/ia_lab2/src/dataGathering/datos2.txt", "r")
    data=archivo.read()
    d=data.split("\n")
    d=d[:len(d)-1]
    pos = []
    self.contador += 1
    for i in d:
      pos.append(i.split(",")[0])
    return pos
  
