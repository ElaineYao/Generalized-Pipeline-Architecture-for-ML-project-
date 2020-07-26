# Generalized-Pipeline-Architecture-for-ML-project
This is a generalized pipeline that can run two different ML applications now. (Traffic prediction & Weather prediction)

It is based on [Simulation of Real-time Traffic Prediction.](https://github.com/ElaineYao/Simulation-of-Real-time-Traffic-Prediction)

The weather prediction project aims to predict the temperature after 6 hours according to the previous 5 days' recorded data. Dataset can be found in [jena_climate_2009_2016.](https://www.kaggle.com/stytch16/jena-climate-2009-2016)

The path for the dataset will serve as the command line parameter when running the program.

# How to run
`python file_reader.py datapath | python preprocess.py type | python train.py type batch_size epochs`

- **datapath:** the path that restores the .csv file, e.g. ./dataset/train.csv
- **type:** the project that will run
  - `traffic` -- the traffic prediction project
  - `weather` -- the weather prediction project
- **batch_size:** the batch_size for training, e.g. 64
- **epochs:** the epochs for training, e.g. 10

# File Structure
- **Pipe line:** This contains `file_reader.py`, `preprocess.py` and `train.py`. To see the dataflow, please refer to [Simulation of Real-time Traffic Prediction.](https://github.com/ElaineYao/Simulation-of-Real-time-Traffic-Prediction)
- **Traffic Prediction:** This contains `utils_traffic.py`, `convert_traffic.py`, `network_traffic.py`. If the command line parameter - type - is traffic, the above functions will be called in the pipe line.
- **Weather Prediction:** This contains `utils_weather.py`, `convert_weather.py`, `network_weather.py`. If the command line parameter - type - is weather, the above functions will be called in the pipe line.
