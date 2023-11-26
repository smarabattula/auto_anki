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
from user_cli import *
import sys
import gpt_prompting as gp
import gpt4 as gp4
from tkinter import messagebox
# from tkinter.ttk import Progressbar
import json
import re

from flask import Flask, render_template, request, jsonify, session

sys.path.append(
    '/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages')


# def process_(file):
#     if file:
#         # lect_name = file.split("/")[-1].split(".")[0]
#         lect_name = os.path.basename(file).split(".")[0]
#         # status_label.update_status("Processing file...",False)

#         if file.split("/")[-1].split(".")[1] == "pdf":
#             pass
#         elif file.split("/")[-1].split(".")[1] == "docx":
#             template = f"soffice --headless --convert-to pdf {file}"
#             os.system(template)
#             file = file[:-5] + ".pdf"

#         raw_data = extract_words(file)
#         raw_data = text_to_groupings(raw_data)
#         keyword_data = wp.extract_noun_chunks(raw_data)
#         keyword_data = wp.merge_slide_with_same_headers(keyword_data)

#         keyword_data = wp.duplicate_word_removal(keyword_data)
#         search_query = wp.construct_search_query(
#             keyword_data)

#         print("process_ function 0")
#         print(request.form)
#         print("process_ function",request.form['source'])
#         source_choice = request.form['source']

#         if source_choice == "Google":
#             with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
#                 # when testing use searchquery[:10 or less].
#                 # Still working on better threading to get faster results
#                 results = executor.map(
#                     get_people_also_ask_links, search_query[:3])
#         elif source_choice == "GPT":
#             with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
#                 results = executor.map(gp.get_gpt_answers, search_query[:3])
#         # print(results)
#         auto_anki_model = get_model()
#         deck = get_deck(deck_name=lect_name)
#         for result in results:
#             for qapair in result:
#                 question = qapair["Question"]
#                 answer = qapair["Answer"]
#                 qa = add_question(
#                     question=f'{question}', answer=f'{answer}', curr_model=auto_anki_model)
#                 deck.add_note(qa)
#         add_package(deck, lect_name)
#     else:
#         print("no file!")


def process_(file):
    try:
        if file:
            # lect_name = file.split("/")[-1].split(".")[0]
            lect_name = os.path.basename(file).split(".")[0]
            # status_label.update_status("Processing file...",False)

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
                    results = executor.map(
                        get_people_also_ask_links, search_query[:3])
            elif source_choice == "GPT":
                with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                    results = executor.map(gp.get_gpt_answers, search_query[:3])
            # print(results)
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
    except Exception as e:
        print("file process_ Error", str(e))
        messagebox.showerror("file process_ Error", str(e))
        # finish_callback()


# Function for processing url
def process_url(url):  # , progress_callback, finish_callback):
    print("processing url", url)
    try:
        results = gp4.get_gpt_link_answers(url)
        results = gp4.get_gpt_link_answers(url)
            # Define a regular expression pattern to match key-value pairs
        pattern = re.compile(r"'(\w+)': '([^']+)'")

        # replace single quotes around question and ans
        # replace double quote within strs with single quote
        results_json = pattern.sub(
            lambda m: '"{}": "{}"'.format(
                m.group(1), m.group(2).replace('"', r"'")
                ),
            results
            )
        print(results_json)
        results_list = json.loads(results_json)
        auto_anki_model = get_model()
        lect_name = url.split("/")[-1]
        deck = get_deck(deck_name=lect_name)
        # print(results)

        for result in results_list:
            # print(result)
            # no error till here
            question = result["Question"]
            answer = result["Answer"]
            # print(question, answer)
            qa = add_question(
                question=f'{question}',
                answer=f'{answer}',
                curr_model=auto_anki_model)
            deck.add_note(qa)
        add_package(deck, lect_name)
        # status_label.update_status("File processed successfully.",True)
    except Exception as e:
        print("process_url error", str(e))
        messagebox.showerror("process_url Error", str(e))

# New function to handle URL input
def process_link(url_input):
    url = url_input.get()
    if url:
        # You might want to add some validation for the URL here
        process_url(url)
    else:
        print("process_link Error", "Please enter a valid URL")
        messagebox.showerror("process_link Error", "Please enter a valid URL")


def new_status():
    return {'message':'Ready','flag':False}


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def index():
    return render_template('index.html',status_label=new_status())


@app.route('/upload/file', methods=['POST'])
# def upload_file():
#     status_label = session.get('status_label', new_status())
#     print("Request",request, request.files)
#     # Check if 'file' is present in the request
#     if request.files['file']:
#         # Process file
#         file = request.files['file']
#         status_label['message'], status_label['flag'] = "Processing file...", False

#         upload_path = os.path.join("uploads", file.filename)
#         if not os.path.exists("uploads"):
#             os.makedirs("uploads")
#         file.save(upload_path)
#         process_(os.path.join("uploads", file.filename))
#         status_label['message'], status_label['flag'] = "File processed successfully!", True

#     session['status_label'] = status_label

#     return jsonify(status_label)

def upload_file():
    try:
        status_label = session.get('status_label', new_status())

        # Check if 'file' is present in the request
        if request.files['file']:
            # Process file
            file = request.files['file']
            status_label['message'], status_label['flag'] = "Processing file...", False

            upload_path = os.path.join("uploads", file.filename)
            if not os.path.exists("uploads"):
                os.makedirs("uploads")
            file.save(upload_path)
            process_(os.path.join("uploads", file.filename))
            status_label['message'], status_label['flag'] = "File processed successfully!", True

        session['status_label'] = status_label

        return jsonify(status_label)
    except Exception as e:
        print("Upload Error", str(e))
        return jsonify(status_label)


@app.route('/upload/url', methods=['POST'])
def upload_url():
    try:
        status_label = session.get('status_label', new_status())
        # Check if 'url' is present in the request
        if request.form['url']:
            # Process URL
            url = request.form['url']
            status_label['message'], status_label['flag'] = "Processing URL...", False
            process_url(url)
            status_label['message'], status_label['flag'] = "URL processed successfully!", True

        session['status_label'] = status_label

        return jsonify(status_label)
    except Exception as e:
        print("Upload URL Error", str(e))
        return jsonify(status_label)


@app.route('/api/status')
def api_get_status():
    # Use session.get to get the user-specific status_label
    status_label = session.get('status_label', new_status())
    return jsonify(status_label)


@app.route('/api/refresh')
def api_refresh_status():
    session['status_label'] = new_status()
    return jsonify(session['status_label'])


if __name__ == '__main__':
    # Set cache control headers
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(host ='0.0.0.0', port = 5000, debug = True)
