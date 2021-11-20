from tkinter import *

# import filedialog module
from tkinter import filedialog
# from user_cli import *
import random
def browseFiles():
    # file = filedialog.askopenfilename(initialdir="/",title="Select a File",filetypes=(("Text files","*.txt*"),("all files","*.*")))
    file = filedialog.askopenfile(parent=window, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
   
    # Change label contents
    text_box = Text(window, height=10, width=50, padx=15, pady=15)
    text_box.insert(1.0, file.name)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=1, row=4)  

    #process_(file)
    # label_file_explorer.configure(text="File Opened: " + filename)


# Create the root window
window = Tk()

canvas = Canvas(window, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)
# Set window title
window.title('Auto-Anki')

# Set window size
window.geometry("500x500")

# Set window background color
window.config(background="white")

instructions = Label(window, text="Select a PDF file on your computer", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

button_explore = Button(window,
                        text="Browse Files",
                        command=browseFiles)

button_exit = Button(window,
                     text="Exit",
                     command=exit)


button_explore.grid(column=1, row=2)

button_exit.grid(column=1, row=3)

# Let the window wait for any events
window.mainloop()