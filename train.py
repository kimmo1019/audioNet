#!/opt/anaconda3/bin/python


from model import KerasModel
from sockDataGenerator import sockDataGenerator
import os

def train(sp=-1):
    model = KerasModel()
    
    train = sockDataGenerator(9009,  50)
    test = sockDataGenerator(9090, 10)
    next(train)
    next(test)
    print('socket esteblish')
    if sp != -1:
        chkp = '.' + os.sep + 'models' + os.sep + 'save_' + str(sp) + '.h5'
        model.load_weights(chkp)
    print('start point: %d'%sp)

    for i in range(sp + 1, 100):
        model.fit_generator(
            generator=train,
            samples_per_epoch=3000,
            nb_epoch=1,
            validation_data=test,
            nb_val_samples=100
        )
        model.save_weights('.' + os.sep + 'models' + os.sep + 'save_' + str(i) + '.h5' )

if __name__ == '__main__':
    train(-1)
