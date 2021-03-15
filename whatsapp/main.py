import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(2)

# if the image looks 70% the same (70% confidence)
position1 = pt.locateOnScreen("./smallyPaperClip.png", confidence=.7)
x = position1[0]
y = position1[1]

# Gets message
def get_message():
  global x, y

  position = pt.locateOnScreen("./greenCircle.png", confidence=.7)
  x = position[0]
  x = position[1]
  # Apple are... Apple. so need to add duration
  pt.moveTo(x, y, duration = .05)
  pt.moveTo(x + 470, y + -45, duration = .05)
  pt.tripleClick()
  pt.rightClick()
  pt.moveRel(12, 15)
  pt.click()
  whatsapp_message = pyperclip.paste()
  # Python String Interpolation
  print(f"msg received: {whatsapp_message}")
  return whatsapp_message

# Posts message
def post_response(msg):
  global x, y
  position = pt.locateOnScreen("./greenCircle.png", confidence=.7)
  x = position[0]
  x = position[1]
  pt.moveTo(x + 470, y + 25, duration = .05)
  pt.click()
  pt.typewrite(msg, interval=.01)

  # pt.typewrite("\n", interval=.01)

# Processes responses

# msg = The msg the person sent you like "How you doing connor?"
def process_response(msg):
  # random num up to 3
  random_no = random.randrange(3)

  # make sure msg is string
  # make lowercase to make sure python can understand
  # if msg has ? respond with...
  if "?" in str(msg).lower():
    return "Don't ask me any question atm"
  else:
    if random_no == 0:
      return "Okay"
    if random_no == 1:
      return "Bare with me 2 secs"
    if random_no == 2:
      return "Bit busy atm"

process_message = process_response(get_message())

post_response(process_message)