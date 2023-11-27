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
import os
from user_cli import *
import sys
import gpt_prompting as gp
import gpt4 as gp4
from tkinter import messagebox
# from tkinter.ttk import Progressbar
import json
from docx2pdf import convert

from flask import Flask, render_template, request, jsonify, session, send_file

sys.path.append(
    '/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages')


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
    return {'message': 'Ready', 'flag': False}


current_filename = None
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def index():
    return render_template('index.html', status_label=new_status())


@app.route('/upload/file', methods=['POST'])
def upload_file():
    try:
        status_label = session.get('status_label', new_status())
        global current_filename

        # Check if 'file' is present in the request
        if request.files['file']:
            # Process file
            file = request.files['file']
            current_filename = file.filename
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
        global current_filename
        status_label = session.get('status_label', new_status())
        # Check if 'url' is present in the request
        if request.form['url']:
            # Process URL
            url = request.form['url']
            current_filename = url.split("/")[-1]
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


@app.route('/download')
def download_apkg():
    global current_filename
    if current_filename:
        current_filename = current_filename.split("/")[-1]
        current_filename = current_filename.split(".")[0]+".apkg"
        # Replace with your file path
        file_path = os.path.join(
            "anki_decks", current_filename)

        return send_file(file_path, as_attachment=True, download_name=current_filename)

    else:
        return "No file uploaded", 400


if __name__ == '__main__':
    # Set cache control headers
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(host='0.0.0.0', port=5000, debug=True)
