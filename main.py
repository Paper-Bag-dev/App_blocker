import sys
from tkinter import *
from Finder import Overlay

win = Tk()
win.title("App Blocker")
win.config(padx=2, pady=2, bg="#65647C")


def open_text():
    text_file = open("test.txt", "r")
    content = text_file.read()
    my_text_box.insert(END, content)
    text_file.close()


def save_text():
    text_file = open("test.txt", "w")
    text_file.write(my_text_box.get(1.0, END))
    text_file.close()


def run_blocker():
    Overlay(my_application=content)

def close_blocker():
    sys.exit()

# Text Box
my_text_box = Text(win, height=10, width=40, bg="#6B728E", highlightcolor="#6B728E")
my_text_box.pack()

open_btn = Button(win, text="Open Text File", command=open_text, highlightcolor="#65647C")
open_btn.pack()


# Save Button
save = Button(win, text="Save File", command=save_text, highlightcolor="#65647C")
save.pack()

run = Button(win, text="Run Blocker", command=run_blocker, highlightcolor="#65647C")
run.pack()

close = Button(win, text="Close Blocker", command=close_blocker)
close.pack()

# Reading the file
text_file = open("test.txt", "r")
content = text_file.read()
text_file.close()

win.mainloop()
