import tkinter
from tkinter import *
import tkinter.font as font
from webscrape import *

global_Label = None
global label2

root = Tk()
root.geometry("500x550")
root.resizable(False, False)
root.title("College Database Webscraper")

# Creates a frame for bottom widgets, then packs them to main screen


frame = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)

f = font.Font(family='Helvetica', size=16, weight="bold")

label_list = []

new_L = Label(frame2)
new_L.config(font=("Montserrat", 12))
new_L.pack(anchor='w', side=LEFT)


def getInput():
    college_name = u_input_box.get()

    global global_Label

    # check for empty input
    if (len(college_name) != 0):
        u_input_box.delete(0, END)

        label2.pack_forget()
        getData(college_name)
    else:
        label2.config(text="Input cannot be empty", font=("Montserrat", 12, font.BOLD), foreground="red")
        label2.pack()


def getData(college_name):
    ret_val = webscrape((college_name))

    if (ret_val == -1):
        label2.config(text="COLLEGE NOT FOUND!", font=("Montserrat", 12, font.BOLD), foreground="red")
        label2.pack()
    else:
        blank = "\n"
        array_string = blank.join(ret_val)
        new_L.configure(text=array_string)


# title text
myLabel = Label(frame3, text="College Database Webscraper")
myLabel.config(font=("Merriweather", 16, font.BOLD))
myLabel.pack()

label2 = Label(frame3, text="Input cannot be empty")
label2.pack_forget()

# input box
u_input_box = Entry(frame, width=30, font=("Montserrat", 12))
u_input_box.pack(padx=10, pady=10, side=tkinter.LEFT)

# fetch button
but1 = Button(frame, text="Fetch", command=getInput)
but1.config(width=10)
but1.pack(side=tkinter.LEFT)

frame3.pack(side=tkinter.TOP)
frame2.pack()
frame.pack(side=tkinter.BOTTOM)


root.mainloop()
