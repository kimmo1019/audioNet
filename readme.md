# audioNet
A deep neural network for audio recognition with online prediction website.
![](https://github.com/kimmo1019/audioNet/blob/master/audioNet.png)


# Requirements
- TensorFlow
- Keras
- flask
- ffmpeg

It has been tested under a Ubuntu system with TensorFlow==1.10.1, Keras=2.1.4

# Data preparation
### Software dependency
Run `bash install.sh` for installing ffmpeg,flask,Keras.
### Data conversion
You should prepare your own data here. In our case, we collected audios of 24 instructioins ($Label:$Instruction):

|Index | Instruction   |       |   |   | 
| ---- |:-------------:| :-----:|:--:|:--:|
| a    |a:蓝牙开机|  |  |   |
| b    |b:蓝牙拨打电话| bb:蓝牙打电话|  |  |
| c    |c:蓝牙接听电话| cc:蓝牙拨打电话| | |
| d    |d:蓝牙拒接|  |  |  |
| f    |f:蓝牙暂停音乐|ff:蓝牙停止音乐| | |
| g    |g:蓝牙上一首|gg:蓝牙上一曲| | |
| h    |h:蓝牙下一首|hh:蓝牙下一曲| | |
| i    |i:蓝牙音量增大|ii:蓝牙声音增大|iii:蓝牙音量增加|iiii:蓝牙声音增加|
| j    |j:蓝牙音量减小|jj:蓝牙声音减小| | |
| k    |k:蓝牙关机| | | |
| l    |l:蓝牙电量提醒|ll:蓝牙还剩多少电|lll:蓝牙还剩多少电量| |

The audio data should be prepared as follows,all the audios are names with their labels. Note that any format (mp3, m4a, webm, wav, etc) of audio is acceptable.
```
raw_data\
         user1\
               a.wav
               b.wav
               cc.wav
               ...
               lll.wav
         user2\
         ...
         userN\
```

Then run `python convert_file.py $raw_data` for uniformly preprocessing data. The raw audios will be transfromed to `.wav`.


# How to train a deep model?

Just run `python train.py` for model training, note that 10% of the training data will be kept for validation.

The weights of model at each epoch will be saved in `models` folder.


Early stopping strategy is used.

# Predicting with a trained models on a web server
We use `flask` framework for quickly establishing a simple web page for online prediction.

Modify `webfront.py`, change `MODEL_ID` to the model index with the highest valiation accuracy.

Then Run `python webfront.py`. The flask app port is set to 9000.

Open a web browser and input URL:http://IP_ADDRESS:9000. 

You can find some basic instructions for deploying audioNet.
![Instruction page](https://github.com/kimmo1019/audioNet/blob/master/ScreenShots/Instruction.png)

Then, You can record a voice directive and upload it for test immediately. It will return the predictive outcome.
![Prediction page](https://github.com/kimmo1019/audioNet/blob/master/ScreenShots/Prediction.png)

# Acknowledgement

This project is suppoorted by Fundamental Industry Training Center in Tsinghua University. Many thanks to Zhen Chen,Wenxun Zheng and Haotian Liu. 




