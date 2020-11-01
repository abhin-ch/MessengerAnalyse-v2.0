import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
from src.formator import main as formator
from src.analysis import main as analysis

import time # testing speed

import src.db as db # database

from shutil import copy

app=Flask(__name__)

app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Get current path
path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')

# Make directory if uploads is not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extension you can set your own
ALLOWED_EXTENSIONS = {'json'}


def allowed_file(filename):
    """ Return True if file is appropriate type in ALLOWED_EXTENSIONS
    """
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_file():
    # Uploading Multiple File
    if request.method == 'POST':

        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


        # Format the Uploaded Files -> Combine, Store and Delete -src/formator.py
        start = time.time()
        data = formator()
        end = time.time() - start

        # debug
        print('Formator time:', end)

        # TODO: upload data to SQLite Database
        start = time.time()

        # create tables, and insert data into database
        db._init('messages.db', data)
        end = time.time() - start
        print("Database init(create table, insert):", end)



        # Run the analysis -src/analysis.py
        start = time.time()
        report = analysis(data)
        end = time.time() - start

        # delete database tables
        db.delete_database('messages.db')

        # debug
        print('Analysis time:', end)

        return render_template('index.html', data = report)

@app.route('/romeo_juliet')
def example_file_1():
    # collect test file
    f = os.path.join('.', 'static', 'test_file', 'shakesphere_romeo_juliet.json')

    # copy test file to uploads folder
    copy(f, os.path.join('.', 'uploads'))

    # # Format the Uploaded Files -> Combine, Store and Delete -src/formator.py
    data = formator()
    db._init('messages.db', data)

    # # Run the analysis -src/analysis.py
    report = analysis(data)

    # delete database
    db.delete_database('messages.db')
    return render_template('index.html', data = report)

@app.route('/theoffice')
def example_file_2():
    # collect test file
    f = os.path.join('.', 'static', 'test_file', 'theoffice.json')

    # copy test file to uploads folder
    copy(f, os.path.join('.', 'uploads'))

    # # Format the Uploaded Files -> Combine, Store and Delete -src/formator.py
    data = formator()
    db._init('messages.db', data)

    # # Run the analysis -src/analysis.py
    report = analysis(data)

    # delete database
    db.delete_database('messages.db')
    return render_template('index.html', data = report)

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=False,threaded=True)
