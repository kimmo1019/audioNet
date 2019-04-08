#!/opt/anaconda3/bin/python
# -*- coding:utf-8 -*-

import os, sys, subprocess
from flask import Flask, request, redirect, flash
from flask import render_template
from werkzeug.utils import secure_filename
import numpy

sys.path.append('augmentation' + os.sep)
from scipy.io import wavfile
from model import KerasModel

UPLOAD_FOLDER = '.' + os.sep + 'tmp'
FFMPEG_PATH='/usr/bin/ffmpeg'
MODEL_ID=17

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def predict(wav_file, modelfile):
    spl, wav = wavfile.read(wav_file)
    wav = wav.reshape([1, -1, 1, 1])

    modelA = KerasModel()
    modelA.load_weights(modelfile)

    result = modelA.predict(wav, 1)
    return numpy.argmax(result, 1)[0]

def command_exists(command):
    return subprocess.call('type ' + command, shell=True, 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

DICT=[
    '蓝牙开机',
    '蓝牙拨打电话',
    '蓝牙打电话',
    '蓝牙接听电话',
    '蓝牙接电话',
    '蓝牙拒接',
    '蓝牙播放音乐',
    '蓝牙开始音乐',
    '蓝牙暂停音乐',
    '蓝牙停止音乐',
    '蓝牙上一首',
    '蓝牙上一曲',
    '蓝牙下一首',
    '蓝牙下一曲',
    '蓝牙音量增大',
    '蓝牙声音增大',
    '蓝牙音量增加',
    '蓝牙声音增加',
    '蓝牙音量减小',
    '蓝牙声音减小',
    '蓝牙关机',
    '蓝牙电量提醒',
    '蓝牙还剩多少电',
    '蓝牙还剩多少电量'
    ]

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html',title='Home')
    

@app.route('/predict', methods=['GET', 'POST'])
def predictAction():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        if file :#and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            fullpath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            if os.path.exists(fullpath) and os.path.isfile(fullpath):
                os.remove(fullpath)
            file.save(fullpath)  # save the uploaded file
            
            if os.path.exists(FFMPEG_PATH) or os.path.exists(FFMPEG_PATH + '.exe'):
                ffmpeg_cmd = ' -i {} -ac 1 -acodec pcm_f32le -ar 44100 {}.wav -v 1'.format(fullpath, fullpath)
                ffmpeg_cmd = FFMPEG_PATH + ffmpeg_cmd
                ffmpeg_cmd = 'echo -e "y\r" | ' + ffmpeg_cmd
                
                os.system(ffmpeg_cmd)
                res = predict(fullpath + '.wav', '.' + os.sep + 'models' + os.sep + 'save_'+ str(MODEL_ID) +'.h5')
            else:
                return 'Unable to find ffmpeg, please install ffmpeg'

            return str(DICT[res])

    return render_template('predictAction.html',title='Prediction')
    #return '''
    #<!doctype html>
    #<title>audioNet Predicting</title>
    #<h1>Upload audio for prediction</h1>
    #<form action="" method=post enctype=multipart/form-data>
    #  <p><input type=file name=file accept='audio/*' capture>
    #     <input type=submit value=Upload>
    #</form>
    #'''

if __name__ == "__main__" :
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(host='0.0.0.0', port=9000)
