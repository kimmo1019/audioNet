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
| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
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

