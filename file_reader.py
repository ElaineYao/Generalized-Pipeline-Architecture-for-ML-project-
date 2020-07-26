# Read the data from .csv
# Output: dataframe of 10 rows every 1 second

import pandas as pd
import time
import sys
import json
from utils import *

def file_reader(datapath):
    df = pd.read_csv(datapath)
    # WARNING: When predicting the weather, the 'step' must be set at least larger than 1500
    # due to the 'multivariate_data' function need some 'past_history' data to return the training data
    step = 2000
    df_len = df.shape[0]

    for i in range(0,df_len,step):
        df_o = pd.DataFrame(columns=df.columns)
        df_o = df[i: i+step]
        inputDict = df_o.to_dict()
        # convert a dict to JSON
        jsonString = json.dumps(inputDict)
        sys.stdout.write(jsonString + '\n')
        sys.stdout.flush()
        time.sleep(1)

if __name__ == '__main__':
    # Argument:
    # datapath : the path that stores the .csv file
    datapath = sys.argv[1]
    file_reader(datapath)

