from win32gui import GetWindowRect, FindWindow
from tkinter import *
# from PIL import ImageTk, Image


class Overlay:
    def __init__(self, my_application):
        self.my_application = my_application
        self.overlay = Tk()
        self.overlay.attributes("-topmost", True)
        self.overlay.config(bg="#6B728E")
        self.clock()

    def clock(self):
        window_handle = FindWindow(None, self.my_application)
        if window_handle:
            left, top, right, bottom = GetWindowRect(window_handle)
            x = right - left
            y = bottom - top
            print(left, top, right, bottom, window_handle)
            self.overlay.overrideredirect(True)
            try:
                self.overlay.geometry(f"{x-15}x{y-45}+{left + 7}+{top + 40}")

            except TclError:
                print("Bad Geometry: ", window_handle)
                self.overlay.geometry("0x0")
        else:
            # print("No window found")
            self.overlay.geometry("0x0")

        self.overlay.overrideredirect(True)
        self.overlay.after(100, self.clock)
        self.overlay.lift()


