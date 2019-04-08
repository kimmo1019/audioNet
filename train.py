#!/opt/anaconda3/bin/python


from model import KerasModel
import os
import numpy as np
from scipy.io import wavfile
from keras.callbacks import EarlyStopping
from keras.callbacks import Callback

class MyCallback(Callback):
    def __init__(self):
        pass
    def on_epoch_end(self, epoch, logs={}):
        self.model.save_weights('./models/save_%d.h5' % epoch)

def preprocess(file_name,length=400000):
    freq, wave_data = wavfile.read('./data/train/%s'%file_name)
    data = np.zeros(length,dtype='float32')
    if len(wave_data)<=length:
        data[:len(wave_data)] = wave_data
    else:
        data = wave_data[:length]
    data = data*1.0/np.max(data)  
    return data

def generate_label(file_name):
    label = np.zeros(24,dtype='int8')
    label_id = int(file_name.split('.')[0].split('_')[-1])
    label[label_id] = 1
    return label

def train(sp=-1):
    model = KerasModel()
    wave_file_list = [item for item in os.listdir('./data/train') if item[-3:]=='wav']
    wave_train_data = list(map(preprocess,wave_file_list))
    wave_train_data = np.array(wave_train_data,dtype='float32')
    wave_train_data.resize((wave_train_data.shape[0],wave_train_data.shape[1],1,1))
    wave_train_label = list(map(generate_label,wave_file_list))
    wave_train_label = np.array(wave_train_label,dtype='int8')
    cb = MyCallback()
    callbacks=[cb,EarlyStopping(monitor='val_acc', patience=4, verbose=1,mode='auto')]
    model.fit(wave_train_data,wave_train_label,batch_size=64,epochs=50,verbose=1,validation_split=0.1,callbacks=callbacks)


if __name__ == '__main__':
    train(-1)
