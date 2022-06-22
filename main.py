import os
from tkinter.filedialog import *
from tkinter import *
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *

def change_color():
    color = colorchooser.askcolor(title="Pick a color to get started")
    text_area.config(fg=color)

def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))

def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)

def open_file():
    filename = askopenfilename(filetypes=[('Text Files (.txt)', '*.txt'), ("all files", "*")])

def save_file():
    filedialog.asksaveasfilename(initialfile='untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    showinfo("Notepad Python Edition", "Using Bro Code Tutorial, I made this Notepad")

def quit():
    window.destroy()

window = Tk()
window.title("Notepad Python")
file = None

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("25")

text_area = Text(window, font=(font_name.get()))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight =1)
text_area.grid(sticky=N + E + S + W)

frame = Frame(window)
frame.grid()

color_button = Button(frame, text="color", command=change_color)
color_button.grid(row=0, column=1)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=2)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_command(label="Copy ALL", command=copy)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)
window.mainloop()










