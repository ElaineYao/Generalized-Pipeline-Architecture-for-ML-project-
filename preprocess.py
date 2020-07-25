from utils import *
import pandas as pd
import sys
import json
from convert_traffic import *

def preprocess(convert_type):
    while True:
        # Convert JSON to dataframe
        jsonString = sys.stdin.readline()
        inputDict = json.loads(jsonString)
        input_temp = pd.DataFrame.from_dict(inputDict)
        # Choose the type of preprocessing
        if convert_type == 'traffic':
            outputDict = convert_traffic(input_temp)
        elif convert_type == 'weather':
            print('**')
        else:
            print('Invalid convert type -- '+convert_type)
        # Convert dict to JSON
        jsonString = json.dumps(outputDict)
        sys.stdout.write(jsonString + "\n")
        sys.stdout.flush()

if __name__ == '__main__':
    # Argument:
    # traffic : stands for traffic prediction project
    # weather : stands for weather prediction project
    convert_type = sys.argv[1]
    preprocess(convert_type)
