from pynput import keyboard
import pyperclip
import sys

c = keyboard.Controller()

def press_callback(key):
    print('{} was pressed'.format(key))
    if key == keyboard.Key.esc:
        return False
    if key == keyboard.Key.scroll_lock:
        data = pyperclip.paste()
        c.type(data)

def release_callback(key):
    print('{} released'.format(key))

l = keyboard.Listener(on_press=press_callback,on_release=release_callback)
l.start()
l.join()
