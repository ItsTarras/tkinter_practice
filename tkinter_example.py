#Tkinter example test

#Imports tkinter, and we can call it using tk.method()
import tkinter as tk
import time

count = 0

def update_clock():
    current_time = time.strftime('%H:%M:%S') # This line grabs the current time
    timeLabel.config(text=f"NZDT: {current_time}") #Update the label
    window.after(1000, update_clock)  #Schedule an update for ONLY update_clock.

def button_clicked():
    global count #Bring the global variable count in here.
    print("Button has been clicked")
    count += 1
    clicked_label.config(text = f"Button has been clicked {str(count)} times!")

#Create a tkinter window:
window = tk.Tk()

#Adds a label to the window.
label = tk.Label(window, text="Hello world")
label2 = tk.Label(window, text = "is the current time.")
timeLabel = tk.Label(window, text="")
clicked_label = tk.Label(window, text="")

#Adds a button to the window.
button = tk.Button(window, text = "Click here!", command = button_clicked)
button.pack(side="bottom")

#This chooses where each label is placed in the window.
#You can choose which side to place from 'top', 'bottom', 'left', or 'right'.
timeLabel.pack(side='top')
label2.pack(side='top')
label.pack(side='top')
clicked_label.pack(side = "right")

#Set the window size:
window.geometry("400x300")

#Update the current time on the window.
update_clock()


#This is the tkinter equivalent to main()
window.mainloop()