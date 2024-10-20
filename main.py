import tkinter as tk
import keyboard
import threading
import time

root = tk.Tk()
root.geometry("600x400")
root.title("ButtonSmasher")
root.resizable(0, 0)
title = tk.Label(text="ButtonSmasher", font=("Arial", 40))
title.pack()
subtitle = tk.Label(text="Created by Powerpellet1077", font=("Arial", 10))
subtitle.pack()
cur_key = ""
def wait_for_key():
    global cur_key
    get_key.config(text=" -- ")
    key = keyboard.read_event()
    if key.event_type == keyboard.KEY_DOWN:
        pressed_key = key.name
        get_key.config(text="Current key: "+pressed_key)
        cur_key = pressed_key
        return
    else:
        return -1

def wait_for_key_hotkey():
    hot_key.config(text=" -- ")
    key = keyboard.read_event()
    if key.event_type == keyboard.KEY_DOWN:
        pressed_key = key.name
        hot_key.config(text="Current key: "+pressed_key)
        try:
            keyboard.remove_hotkey(flip)
        except:
            pass
        keyboard.add_hotkey(pressed_key, flip)
        return
    else:
        return -1

running = False
def run():
    global running
    if running and cur_key:
        keyboard.press_and_release(cur_key)
    root.after(10, run)


def flip():
    global running
    running = not running

threading.Thread(target=run, daemon=True).start()

get_key = tk.Button(text="Press to select a key", command=lambda: threading.Thread(target=wait_for_key).start())
get_key.pack()
hot_key = tk.Button(text="Press to select the hotkey", command=lambda: threading.Thread(target=wait_for_key_hotkey).start())
hot_key.pack()

keyboard.add_hotkey("f", flip)
root.mainloop()