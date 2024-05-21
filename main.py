import tkinter as tk
from tkinter import messagebox
import pygame
import os

user = os.getlogin()

pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
pygame.event.wait()

def como():
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.attributes('-fullscreen', True)
    root.overrideredirect(True)
    root.configure(background='black')
    label = tk.Label(root, text="o_O", font=("Helvetica", 48), fg="white", bg="black")
    label.pack(expand=True)
    root.bind("<Escape>", lambda e: root.quit())
    
    def on_close():
        root.destroy()
        como()
    
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

como()
