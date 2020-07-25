# Generalized-Pipeline-Architecture-for-ML-project
This is a generalized pipeline that can run two different ML applications now. (Traffic prediction & Weather prediction)

It is based on [Simulation of Real-time Traffic Prediction](https://github.com/ElaineYao/Simulation-of-Real-time-Traffic-Prediction)

# How to run
`python file_reader.py datapath | python preprocess.py type | python train.py type`

- **datapath:** the path that restores the .csv file, e.g. ./dataset/train.csv
- **type:** the project that will run
  - `traffic` -- the traffic prediction project
  - `weather` -- the weather prediction project
