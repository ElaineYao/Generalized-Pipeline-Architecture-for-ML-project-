from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.optimizers import RMSprop

def network_weather(x_train):
    single_step_model = Sequential()
    single_step_model.add(LSTM(32, input_shape=x_train.shape[-2:]))
    single_step_model.add(Dense(1))

    single_step_model.compile(RMSprop(), loss='mae')
    return single_step_model

