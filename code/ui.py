# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *

# import filedialog module
from tkinter import filedialog
from user_cli import *
import random


def process_(file):

    lect_name =  str(random.randint(0,10000))
    raw_data = extract_words(file)
    raw_data = text_to_groupings(raw_data)
    keyword_data = wp.extract_noun_chunks(raw_data)
    keyword_data = wp.merge_slide_with_same_headers(keyword_data)

    keyword_data = wp.duplicate_word_removal(keyword_data)
    search_query = wp.construct_search_query(
        keyword_data)
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # when testing use searchquery[:10 or less].
        # Still working on better threading to get faster results
        results = executor.map(get_people_also_ask_links, search_query[:3])

    auto_anki_model = get_model()
    deck = get_deck(deck_name=lect_name)
    for result in results:
        for qapair in result:
            question = qapair["Question"]
            answer = qapair["Answer"]
            qa = add_question(question=f'{question}', answer=f'{answer}', curr_model=auto_anki_model)
            deck.add_note(qa)

    add_package(deck, lect_name)


# Function for opening the
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))

    # Change label contents

    process_(filename)
    label_file_explorer.configure(text="File Opened: " + filename)


# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("500x500")

# Set window background color
window.config(background="white")

# Create a File Explorer label
label_file_explorer = Label(window,
                            text="File Explorer using Tkinter",
                            width=100, height=4,
                            fg="blue")

button_explore = Button(window,
                        text="Browse Files",
                        command=browseFiles)

button_exit = Button(window,
                     text="Exit",
                     command=exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column=1, row=1)

button_explore.grid(column=1, row=2)

button_exit.grid(column=1, row=3)

# Let the window wait for any events
window.mainloop()