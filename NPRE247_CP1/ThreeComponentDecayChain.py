# Import Libraries
import sys
import numpy as np
import matplotlib.pyplot as plt

# Deine Functions


# Open file and read to associated variables
f = open(sys.argv[1], "r")
Input = f.readlines()
f.close()

lambdaA = Input[0]
lambdaB = Input[1]
N_A0 = Input[2]
N_B0 = Input[3]
N_C0 = Input[4]
deltat = Input[5]
T_final = Input[6]

if __name__ == "__main__":