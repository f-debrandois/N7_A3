from flask import Flask, request, render_template, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import os
import subprocess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'jar'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def list_files(directory):
    return os.listdir(directory)

@app.route('/')
def index():
    data_files = list_files(os.path.join(app.config['UPLOAD_FOLDER'], 'data'))
    program_files = list_files(os.path.join(app.config['UPLOAD_FOLDER'], 'programs'))
    return render_template('index.html', data_files=data_files, program_files=program_files)

@app.route('/upload_data', methods=['POST'])
def upload_data():
    if 'file' not in request.files or 'hdfs_path' not in request.form:
        return "No file or HDFS path provided", 400
    file = request.files['file']
    hdfs_path = request.form['hdfs_path']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'data', filename))
        result = subprocess.run(['hdfs', 'dfs', '-put', os.path.join(app.config['UPLOAD_FOLDER'], 'data', filename), hdfs_path], capture_output=True, text=True)
        if result.returncode != 0:
            return f"Error uploading to HDFS: {result.stderr}", 500
        return redirect(url_for('index'))
    return "Invalid file type", 400

@app.route('/upload_program', methods=['POST'])
def upload_program():
    if 'file' not in request.files:
        return "No file provided", 400
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'programs', filename))
        return redirect(url_for('index'))
    return "Invalid file type", 400

@app.route('/execute_job', methods=['POST'])
def execute_job():
    if not all(k in request.form for k in ('program', 'input_path', 'output_path')):
        return "Missing form parameters", 400
    program = request.form['program']
    input_path = request.form['input_path']
    output_path = request.form['output_path']
    program_path = os.path.join(app.config['UPLOAD_FOLDER'], 'programs', program)
    if not os.path.exists(program_path):
        return "Program not found", 404
    result = subprocess.run(['spark-submit', '--class', 'org.apache.spark.examples.SparkPi', program_path, input_path, output_path], capture_output=True, text=True)
    if result.returncode != 0:
        return f"Error executing job: {result.stderr}", 500
    return redirect(url_for('index'))

@app.route('/delete_data/<filename>', methods=['POST'])
def delete_data(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'data', filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    result = subprocess.run(['hdfs', 'dfs', '-rm', os.path.join(app.config['UPLOAD_FOLDER'], 'data', filename)], capture_output=True, text=True)
    if result.returncode != 0:
        return f"Error deleting HDFS file: {result.stderr}", 500
    return redirect(url_for('index'))

@app.route('/delete_program/<filename>', methods=['POST'])
def delete_program(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'programs', filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
