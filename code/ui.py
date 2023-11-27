# MIT License
#
# Copyright 2023 auto_anki
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from ui_main import process_, process_url
import random
import json
from tkinter.ttk import Progressbar
import gpt4 as gp4
import gpt_prompting as gp
import threading
import sys
from docx2pdf import convert
from tkinter import filedialog, Tk, ttk, Label, Button, StringVar, OptionMenu, messagebox, Text
from tkinter import *
from tkinter import filedialog
from user_cli import *
from PIL import ImageTk
import os

sys.path.append(
    '/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages')


# Function to call process_url
def process_link():
    url = url_input.get()
    c_count = cards_count.get()
    if url:
        # You might want to add some validation for the URL here
        process_url(url, c_count)
    else:
        messagebox.showerror("Error", "Please enter a valid URL")


# def update_progress(n):
#     progress['value'] = n  # Update the progress bar's value
#     progress_label['text'] = f"{n}/100"  # Update the label text
#     window.update_idletasks()

# Function to show finish message
def on_finish():
    # progress['value'] = 0
    messagebox.showinfo(
        "Success", "The Anki deck has been created successfully.")

# Function for opening the file explorer window


def browseFiles():
    # file = filedialog.askopenfilename(initialdir="/",title="Select a File",filetypes=(("Text files","*.txt*"),("all files","*.*")))
    file = filedialog.askopenfilename(parent=window, title="Choose a file", filetypes=[
                                      ("Doc file", "*.docx"), ("Pdf file", "*.pdf"), ("PowerPoint file", "*.pptx")])

    if file:
        text_box = Text(window, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, file)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=0, row=3)
        c_count = int(cards_count.get())
        process_(file, c_count)


def update_status(message):
    status_label.config(text=message)
    window.update_idletasks()


# Create the root window
window = Tk()
# window.minsize(width=450, height=450)
window.config(background="#515A5A")
# Set window title
window.title('Auto-Anki')

# Set window size
window.geometry("500x550")
canvas = Canvas(window, bg='#515A5A')

# Configure the grid to be responsive
number_of_rows = 7
number_of_columns = 3

for i in range(number_of_rows):
    window.grid_rowconfigure(i, weight=1)

for j in range(number_of_columns):
    window.grid_columnconfigure(j, weight=1)

canvas.grid(row=0, column=0, rowspan=number_of_rows,
            columnspan=number_of_columns, sticky='nsew')
# set logo
logo = ImageTk.PhotoImage(file='code/Auto_Anki_Logo.jpg')
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(column=0, row=0, columnspan=3)

instructions = Label(
    window, text="    Select file to upload: ", font="Raleway")
instructions.grid(column=0, row=2, sticky='w')

button_explore = Button(window,
                        text="Browse Files",
                        command=browseFiles)

source_choice = StringVar(window)  # Variable to hold the choice
sources = ["Google", "GPT"]  # List of choices
source_choice.set(sources[0])  # Set default value to Google

source_dropdown = OptionMenu(window, source_choice, *sources)
source_dropdown_label = Label(
    window, text="    Choose an API source:", font="Raleway")

source_dropdown_label.grid(column=0, row=1, sticky='w')
source_dropdown.grid(column=1, row=1)


style = ttk.Style(window)
# Set the theme to the default theme
style.theme_use('default')
style.configure('TProgressbar', thickness=10)

# Add a text field for URL input
url_input = Entry(window, width=30)

# Add a text field for no.of flash cards input
instructions2 = Label(
    window, text="    Number of flash cards: ", font="Raleway")
cards_count = Entry(window, width=5)

# Add a text field for URL input
instructions1 = Label(
    window, text="    Process URL: ", font="Raleway")

# Add a button to process the URL
button_process_url = Button(window,
                            text="->",
                            command=process_link)

# Status
status_label = Label(window, text="Ready", bd=1,
                     relief="sunken")  # , anchor="w")
status_label.grid(column=0, row=5, columnspan=3,
                  sticky="we", padx=(10, 10), pady=(10, 10))
status_label.config(justify="center")

button_exit = Button(window,
                     text="Exit",
                     command=exit)

button_explore.grid(column=1, row=2)
button_exit.grid(column=0, row=6, columnspan=3)
url_input.grid(column=1, row=3)
instructions2.grid(column=0, row=4, sticky='w')  # Number of Flash Cards
cards_count.grid(column=1, row=4)
instructions1.grid(column=0, row=3, sticky='w')  # Process URL
button_process_url.grid(column=2, row=3)


# Let the window wait for any events
window.mainloop()
