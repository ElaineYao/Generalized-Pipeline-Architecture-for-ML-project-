from utils import *
from network_traffic import *
import pandas as pd
import sys
import json

def train(network_type, batch, epo):
    while True:
        jsonString = sys.stdin.readline()
        dict = json.loads(jsonString)

        x_train = np.array(dict['x_train'])
        x_val = np.array(dict['x_val'])
        x_test = np.array(dict['x_test'])
        y_train = np.array(dict['y_train'])
        y_val = np.array(dict['y_val'])
        y_test = np.array(dict['y_test'])

        if network_type == 'traffic':
            model = network_traffic()
        elif network_type == 'weather':
            print('**')
        else:
            print('Invalid network type -- ' + network_type)

        history = model.fit(x = x_train, y = y_train, validation_data = (x_val, y_val),
                         batch_size=int(batch),
                          epochs=int(epo))
        # Calculate its accuracy on testing data
        _,acc = model.evaluate(x_val, y_val)

        print('The accuracy on the validation data is {}%.'.format(acc*100))
        # Save the model
        model.save('model1_10epoch.h5')

if __name__ == '__main__':
    # Argument:
    # traffic : stands for traffic prediction project
    # weather : stands for weather prediction project
    network_type = sys.argv[1]
    # e.g batch = 64
    batch = sys.argv[2]
    # e.g epo = 10
    epo = sys.argv[3]
    train(network_type, batch, epo)


