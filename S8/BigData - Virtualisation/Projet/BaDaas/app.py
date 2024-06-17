from flask import Flask, request, render_template, redirect, url_for, jsonify
import os
import subprocess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

def list_files(directory):
    return os.listdir(directory)

@app.route('/')
def index():
    data_files = list_files(os.path.join(app.config['UPLOAD_FOLDER'], 'data'))
    program_files = list_files(os.path.join(app.config['UPLOAD_FOLDER'], 'programs'))
    return render_template('index.html', data_files=data_files, program_files=program_files)

@app.route('/upload_data', methods=['POST'])
def upload_data():
    file = request.files['file']
    hdfs_path = request.form['hdfs_path']
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'data', file.filename))
    subprocess.run(['hdfs', 'dfs', '-put', os.path.join(app.config['UPLOAD_FOLDER'], 'data', file.filename), hdfs_path])
    return redirect(url_for('index'))

@app.route('/upload_program', methods=['POST'])
def upload_program():
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'programs', file.filename))
    return redirect(url_for('index'))

@app.route('/execute_job', methods=['POST'])
def execute_job():
    program = request.form['program']
    input_path = request.form['input_path']
    output_path = request.form['output_path']
    program_path = os.path.join(app.config['UPLOAD_FOLDER'], 'programs', program)
    subprocess.run(['spark-submit', '--class', 'org.apache.spark.examples.SparkPi', program_path, input_path, output_path])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
