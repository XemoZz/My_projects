import webbrowser
import random
import string
from pynput import keyboard

def generate_random_string(length):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def open_random_page():
    random_string = generate_random_string(6)
    url = "https://prnt.sc/" + random_string
    webbrowser.open(url)

def on_press(key):
    if key == keyboard.Key.tab:
        open_random_page()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
        