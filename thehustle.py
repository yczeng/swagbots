import webbrowser
import subprocess
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

m = PyMouse()
k = PyKeyboard()


with open('names.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
names = [x.strip().lower() for x in content]

for name in names:
	email = name + '@gmail.com'
	webbrowser.open_new("http://ambassadors.thehustle.co/?ref=137b4eea53")
	time.sleep(5)
	
	k.tap_key(k.tab_key)
	k.type_string(email)
	k.tap_key(k.enter_key)

	time.sleep(5)
	k.press_key(k.control_key)
	k.tap_key('w')
	k.release_key(k.control_key)

