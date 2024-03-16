#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

mainWindow = tk.Tk()
mainWindow.title('Demo')
mainWindow.geometry('300x150')

title_label = ttk.Label(master = mainWindow, text = 'Miles to Kilometers', font = 'Calibri 24 bold')
title_label.pack(pady = 10)

# Input Field
input_frame = ttk.Frame(master = mainWindow)
entry = ttk.Entry(master = input_frame)
button = ttk.Button(master = input_frame, text = 'Convert')
entry.pack(side = 'left', padx = 10 )
button.pack(side='left')
input_frame.pack(pady = 10)

# Output label
output_label = ttk.Label(master = mainWindow, text = 'Output', font = 'Calibri 24')
output_label.pack()

# Run
mainWindow.mainloop()