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

import os
from PIL import ImageTk
from user_cli import *
from tkinter import filedialog
from tkinter import *
from docx2pdf import convert
import sys
import gpt_prompting as gp

from flask import Flask, render_template, request

sys.path.append(
    '/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages')

# import filedialog module


def process_(file):

    if file:
        lect_name = os.path.basename(file)
        if file.split("/")[-1].split(".")[1] == "pdf":
            pass
        elif file.split("/")[-1].split(".")[1] == "docx":
            template = f"soffice --headless --convert-to pdf {file}"
            os.system(template)
            file = file[:-5] + ".pdf"

        raw_data = extract_words(file)
        raw_data = text_to_groupings(raw_data)
        keyword_data = wp.extract_noun_chunks(raw_data)
        keyword_data = wp.merge_slide_with_same_headers(keyword_data)

        keyword_data = wp.duplicate_word_removal(keyword_data)
        search_query = wp.construct_search_query(
            keyword_data)

        source_choice = request.form['source']

        if source_choice == "Google":
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                # when testing use searchquery[:10 or less].
                # Still working on better threading to get faster results
                results = executor.map(get_people_also_ask_links, search_query[:3])
        elif source_choice == "GPT":
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                results = executor.map(gp.get_gpt_answers, search_query[:3])

        auto_anki_model = get_model()
        deck = get_deck(deck_name=lect_name)
        for result in results:
            for qapair in result:
                question = qapair["Question"]
                answer = qapair["Answer"]
                qa = add_question(
                    question=f'{question}', answer=f'{answer}', curr_model=auto_anki_model)
                deck.add_note(qa)

        add_package(deck, lect_name)

# Function for opening the
# file explorer window

# def browseFiles():
#     # file = filedialog.askopenfilename(initialdir="/",title="Select a File",filetypes=(("Text files","*.txt*"),("all files","*.*")))
#     file = filedialog.askopenfilename(parent=window, title="Choose a file", filetypes=[
#                                       ("Doc file", "*.docx"), ("Pdf file", "*.pdf")])

#     # Change label contents
#     text_box = Text(window, height=10, width=50, padx=15, pady=15)
#     text_box.insert(1.0, file)
#     text_box.tag_configure("center", justify="center")
#     text_box.tag_add("center", 1.0, "end")
#     text_box.grid(column=0, row=3)
#     process_(file)

# # Create the root window
# window = Tk()
# # window.minsize(width=450, height=450)
# window.config(background="#ebeceb")

# canvas = Canvas(width=600, height=400)
# canvas.grid(columnspan=2, rowspan=4)
# # Set window title
# window.title('Auto-Anki')

# # Set window size
# window.geometry("500x500")

# # set logo
# logo = ImageTk.PhotoImage(file='code/Auto_Anki_Logo.jpg')
# logo_label = Label(image=logo)
# logo_label.image = logo
# logo_label.grid(column=0, row=0)

# instructions = Label(
#     window, text="Select a PDF file on your computer", font="Raleway")
# instructions.grid(column=0, row=1)

# button_explore = Button(window,
#                         text="Browse Files",
#                         command=browseFiles)

# source_choice = StringVar(window)  # Variable to hold the choice
# sources = ["Google", "GPT"]  # List of choices
# source_choice.set(sources[0])  # Set default value to Google

# source_dropdown = OptionMenu(window, source_choice, *sources)
# source_dropdown_label = Label(
#     window, text="Choose an API source:", font="Raleway")

# source_dropdown_label.grid(column=0, row=2)
# source_dropdown.grid(column=0, row=3)


# button_exit = Button(window,
#                      text="Exit",
#                      command=exit)

# button_explore.grid(column=0, row=4)
# button_exit.grid(column=0, row=5)

# # Let the window wait for any events
# window.mainloop()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    print(os.path.exists("./uploads"))
    if not os.path.exists("./uploads"):
        os.makedirs("uploads")
    file.save(os.path.join("uploads", file.filename))
    process_(os.path.join("uploads",file.filename))
    return "File processed successfully!"

if __name__ == '__main__':
    app.run(debug=True)
