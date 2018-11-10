
import os
from flask import Flask, send_file, request, jsonify
from werkzeug.exceptions import BadRequest
from werkzeug.utils import secure_filename


from test_image import deti
import multiprocessing
import time

print("outside attendance")

# Example
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg','png'])
app = Flask(__name__)


@app.route('/', methods=["POST"])
def attendance():
    print("inside attendance")
    # check if the post request has the file part
    input_file = request.files.get('file')
    if not input_file:
        return BadRequest("File not present in request")

    filename = secure_filename(input_file.filename)
    if filename == '':
        return BadRequest("File name is not present in request")
    if not allowed_file(filename):
        return BadRequest("Invalid file type")

    input_filepath = os.path.join('./images/', filename)
    input_file.save(input_filepath)
    p = multiprocessing.Process(target=deti, args=(input_filepath,))
    p.start()
    time.sleep(25)
    p.terminate()
    file1 = open("demofile.txt","r") 
    ret_var=file1.readlines()
    file1.close()
    return jsonify(ret_var)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
    