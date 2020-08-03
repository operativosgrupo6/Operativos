import datetime
from pynput.keyboard import Listener 

def key_recoder(key):
	print(key)

with Listener(on_press=key_recoder) as l:
	l.join()

