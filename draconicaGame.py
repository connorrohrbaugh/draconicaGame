#####################
##    DRACONICA    ##
##     TAYLOR      ##
##     4/4/14      ##
#####################

#IMPORT STUFF
from graphics import *
import random
import time
import math

#GET DISTANCE
def distance(x1,y1,x2,y2):
  dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
  return dist

#GET THE DISTANCE BETWEEN 2 POINTS
def distanceBetweenPts(p1,p2):
  return distance(p1.getX(),p1.getY(),p2.getX(),p2.getY()

#SETUP WINDOW HERE
def windowInitializer():
  win = GraphWin("Draconica: The Attack of the Wyrm", 600, 600)
  win.setCoords(0,0, 30,30)
  #DRAW ENTRY BOX (W/ BACKGROUND)
  i1 = Image(15,15)

  return win





def main():
  #PUT STUFF HERE
main()
