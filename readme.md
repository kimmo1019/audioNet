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
Run `bash install.sh` for installing ![ffmpeg](https://ffmpeg.org/),flask.
### Data conversion
You should prepare your own data here. In our case, we collected audios of 24 instructioins:

|Index | Instruction   |       |   |   | 
| ---- |:-------------:| -----:|--:|--:|
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

`python convert_file.py $data_folder` for uniformly preprocessing data.

# Step 2. How to train a deep model?
Just run `python train.py` for model training, note that 10% of the training data will be kept for validation.
The weights of model at each epoch will be saved in `models` folder.
Early stopping strategy is used.

* NOTE: the wav file must be encoded by 16 bit signed integer, mono-channeled and at a sampling rate of 16000.

# Step 3. Predicting with a trained models on a web server
## Step 3.1 Select Checkpoint for Evaluation
Modify `webfront.py`, change `MODEL_ID` to yours.

## Step 3.2 Run `python webfront.py`. 
Open a web browser and input URL:http://IP_ADDRESS:9000. 

You can record a voice directive and upload it for test immediately. 

*It requires `[ffmpeg]`(https://ffmpeg.org/) for audio file format convertion.

# Step 4. How to deploy your model in mobile? 
*  Convert model file *.h5 to *.pb file 
*  Place your *.pb file where you want to deploy.
*  See Android mobile example: [androidAudioRecg](http://gitlab.icenter.tsinghua.edu.cn/saturnlab/androidAudioRecg)

`$ python ./create_pb.py  XX`

