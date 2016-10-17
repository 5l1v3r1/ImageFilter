#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Image Filter

Author:
Last modified:
Website:
"""

from tkinter import *
from tkinter import ttk
from tkFileDialog import askopenfilename
from PIL import Image, ImageTk
import numpy as np
from cv2 import * #Import functions from OpenCV
import cv2

class ImageFilter(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.filename = ""
        self.initUI()

    def initUI(self):
        self.button = Button(text = "Dosya sec", command = self.load_file, width = 20)
        self.button.grid(row=0, column=0)

        self.v = IntVar()
        self.radio = Radiobutton(text="1", variable=self.v, value=1, command=self.onClick)
        self.radio.grid(row=1, column=0)

        self.radio = Radiobutton(text="2", variable=self.v, value=2, command=self.onClick)
        self.radio.grid(row=2, column=0)

        self.radio = Radiobutton(text="3", variable=self.v, value=3, command=self.onClick)
        self.radio.grid(row=3, column=0)

        self.radio = Radiobutton(text="4", variable=self.v, value=4, command=self.onClick)
        self.radio.grid(row=4, column=0)

    def load_file(self):
        self.filename = askopenfilename()

        if self.filename:
            try:
                image = Image.open(self.filename)
                self.photo = ImageTk.PhotoImage(image)
                label = Label(image=self.photo)
                label.image = self.photo
                label.grid(row=5, column=0)
            except:
                pass
                return

    def onClick(self):
        if self.v.get():
            print str(self.v.get())
            if self.filename:
                try:
                    image = Image.open(self.filename)
                    self.photo = ImageTk.PhotoImage(image)
                    label = Label(image=self.photo)
                    label.image = self.photo
                    label.grid(row=6, column=0)
                except:
                    pass
                    return
        else:
            print str(self.v.get())

def main():
    root = Tk()
    root.title = "Image Filter"
    root.geometry("900x600+300+300")
    app = ImageFilter(root)
    root.mainloop()

if __name__ == '__main__':
    main()