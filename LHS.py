import numpy as np
import pandas as pd
from pyDOE import *
from scipy.stats import qmc
import sys
import os

cwd = os.getcwd()


'''
Hailing Jia (h.jia@sron.nl)
2025-04-20

This script creats PPE_values.txt/PPE_values.csv according to the parameters you have set in the parameters_range_list.txt file.

The parameters_range_list.txt defines the parameter names and their minimum and maximum values.

'''
def str2bool(value):
    return str(value).strip().lower() in ("true", "1", "yes", "y")

def read_param_settings(file_path):
    param_ranges = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Skip lines starting with '#'
            if line.strip().startswith('#'):
                continue
            parts = line.split()
            if len(parts) == 3:  #0: param name, 1: min, 2: max
                param_name = parts[0]
                param_range = (float(parts[1]), float(parts[2]))
                param_ranges[param_name] = param_range
    return param_ranges


def main():

    try:
        n_simulations = int(input("Enter number of simulations you wish to perform: "))
        write2txt = str2bool(input("Write to PPE_values.txt file? (y/n): "))
        write2csv = str2bool(input("Write to PPE_values.csv file? (y/n): "))
    except Exception as e:
        print(f"Invalid input: {e}")
        return

    #Read parameter
    param_file = os.path.join(cwd, "parameters_range_list.txt")
    param_ranges = read_param_settings(param_file)

    l_bound = np.array([low for low, _, in param_ranges.values()])
    u_bound = np.array([high for _, high in param_ranges.values()])
    names = np.array(list(param_ranges.keys()))

    #Latin Hypercube Sampling
    np.random.seed(1000)
    n_params = len(param_ranges)
    #n_simulations = 39  # or get from file or input

    lhs_sample = lhs(n_params, samples=n_simulations, criterion='maximin')
    rescaled_sample = qmc.scale(lhs_sample, l_bound, u_bound)

    #to DataFrame
    df = pd.DataFrame(rescaled_sample, columns=names)
    df.index = [f"exp_{i}" for i in range(1, n_simulations + 1)]
    df[["INSTALL", "START", "END"]] = 0
    df.index.name = '0'

    #write to csv /txt
    if write2csv:
        df.to_csv("PPE_values.csv", index=True, header=True, float_format="%.6f")
        print("PPE_values.csv written successfully.")

    if write2txt:
        df.to_csv("PPE_values.txt", sep=" ", index=True, header=True, float_format="%.6f")
        print("PPE_values.txt written successfully.")

if __name__ == "__main__":
    main()