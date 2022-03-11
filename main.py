#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import binascii
from tkinter import *

f = open('image.txt', 'r')
image = f.read()

filename = image
with open(filename, 'rb') as f:
    content = f.read()

lines = [binascii.hexlify(content)]
with open('hexValue.txt', 'wb') as f1:
    for line in lines:
        line.split(bytes(16), 16)
        f1.write(line)

print("\033[1;31m #######    ###    ###     ######    ######    #######     #######     #######\n"
      "###         ###    ###    ###       ###        ###        ###         ###\n"
      " #######    ###    ###   ###       ###         #######     #######     #######\n"
      "      ###   ###    ###    ###       ###        ###              ###         ###\n"
      "#######      ########      ######    ######    #######    #######     #######\n"
      "\n\n\nSuccessfully converted your image to hex value.. \n"
      "Check it in your installed folder\\hexValue.txt\n"
      "If output file not in here please select your image path correctly in image.txt file")

def openfile():
    tf = open('hexValue.txt', 'r')
    data = tf.read()
    txt_area.insert(END, data)
    tf.close()


ws = Tk()
ws.title("Hex Value")
ws.geometry("1200x600")
ws['bg'] = '#000000'


txt_area = Text(ws, width=120, height=30)
txt_area.pack(pady=20)


Button(
    ws,
    text="Open",
    command=openfile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)


ws.mainloop()