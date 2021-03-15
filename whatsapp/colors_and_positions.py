import pyautogui as pt
from time import sleep

while True:
  # tells us position of mouse pointer
  posXY = pt.position()
  # show color of what cursor is pointer
  print(posXY, pt.pixel(posXY[0], posXY[1]))
  # show every 2 seconds
  sleep(2)
  if posXY[0] == 0:
    break