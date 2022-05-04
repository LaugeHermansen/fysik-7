#%%

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def preprocess(data_filename, desired_datasets):
    if "processed_data" not in os.listdir(): os.mkdir("processed_data")
    data = pd.read_csv(data_filename if ".csv" == data_filename[:-4] else data_filename + ".csv")
    for data_set_number in desired_datasets:
        angle_col = data[f"Data Set {data_set_number}:Angle(rad)"]
        pressure_col = data[f"Data Set {data_set_number}:Pressure(kPa)"]
        time_col = data[f"Data Set {data_set_number}:Time(s)"]
        max_vol = 44*1e-6
        min_vol = 32*1e-6
        max_angle = angle_col.max()
        min_angle = angle_col.min()
        mean_temp = data[f"Data Set {data_set_number}:Temperature 1(°C)"].mean()
        var_temp  = data[f"Data Set {data_set_number}:Temperature 1(°C)"].var()

        volume_col = (angle_col-min_angle)*(max_vol - min_vol)/(max_angle - min_angle) + min_vol

        output = pd.concat((pressure_col, volume_col), axis = 1)
        output.to_csv(f"processed_data/Experiment_number={data_set_number:02}_mean_temp={mean_temp:3.0f},var_temp={var_temp:1.2f}.csv")


# preprocess("experiment_1_no_resistance-btw_first_one_is_crappy", "without_voltage", range(2,5))
preprocess("physics_shit_baby_shoutout_to_sterling", (2,3,4,7,8,10))

#%%
