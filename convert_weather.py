import numpy as np
import pandas as pd
from utils_weather import *
import tensorflow as tf
from sklearn.model_selection import train_test_split

def convert_weather(df):
    # Choose features
    features_considered = ['p (mbar)', 'T (degC)', 'rho (g/m**3)']
    features = df[features_considered]
    features.index = df['Date Time']
    # Normalization
    dataset = features.values
    data_mean = dataset.mean(axis=0)
    data_std = dataset.std(axis=0)
    dataset = (dataset - data_mean) / data_std  # List
    target_label = dataset[:, 1]
    # Number of observations sampled every hour (6*24*5)
    past_history = 720
    # Number of observations used to predict the label for a datapoint (6*12)
    future_target = 72
    # Step size to sample the past observation
    STEP = 6
    TRAIN_VAL_DATA = 50000
    x_data_single, y_data_single = multivariate_data(dataset, target_label, 0,
                                                       None, past_history,
                                                       future_target, STEP,
                                                       single_step=True)
    # Split the data into training set, test set and validation set
    x_train_tmp, x_test, y_train_tmp, y_test = train_test_split(x_data_single, y_data_single, test_size=0.2, random_state=42)
    x_train, x_val, y_train, y_val = train_test_split(x_train_tmp, y_train_tmp, test_size=0.2, random_state=55)

    outputDict = {'x_train': x_train.tolist(),
                  'x_val': x_val.tolist(),
                  'x_test': x_test.tolist(),
                  'y_train': y_train.tolist(),
                  'y_val': y_val.tolist(),
                  'y_test': y_test.tolist()}
    return outputDict

