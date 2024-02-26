# Import Libraries

import sys
import numpy as np
import matplotlib.pyplot as plt
import json

# Deine Functions

def AnalyticalA(T):
    return N_A0 * np.exp(-lambdaA*T)

def AnalyticalB(T):
    return (lambdaA/(lambdaA+lambdaB))*N_A0*(np.exp(-lambdaA*T)-np.exp(-lambdaB*T)) + N_B0

def AnalyticalC(T):
    return N_B0 - N_B0 * np.exp(-lambdaB*T) + N_C0

def DerivativeA(T):
    return -lambdaA * N_A0 * np.exp(-lambdaA*T)


# Open file and read to associated variables

f = open(sys.argv[1], "r")
Input = f.readlines()
f.close()

halfA = Input[0]
halfB = Input[1]
N_A0 = Input[2]
N_B0 = Input[3]
N_C0 = Input[4]
deltat = Input[5]
T_final = Input[6]

# Define Variables

lambdaA = np.log(2)/halfA
lambdaB = np.log(2)/halfB

analytical_sol_A = AnalyticalA(T_final)
analytical_sol_B = AnalyticalB(T_final)
analytical_sol_C = AnalyticalC(T_final)

timestep = np.linespace(0,T_final,T_final/deltat)
timestep2 = np.linespace(0,T_final,T_final/(deltat/2))
timestep3 = np.linespace(0,T_final,T_final/(deltat/4))

# Set up Numerical Analysis Matricies

nA = np.zeros(T_final/deltat)
nA[0] = N_A0
nB = np.zeros(T_final/deltat)
nB[0] = N_B0
nC = np.zeros(T_final/deltat)
nC[0] = N_C0

# Fill in nA, nB, nC

for i in range(len(nA)-1):
    nA[i+1] = -lambdaA * nA[i] * deltat + nA[i]

for i in range(len(nB)-1):
    nB[i+1] = lambdaA*nA[i] * deltat - lambdaB*nB[i] * deltat + nB[i]

for i in range(len(nC)-1):
    nC[i+1] = lambdaB*nB[i] + nC[i]


# Create Dictionary to Read to JSON

JSON = {}
JSON["timestep"] = timestep
JSON["timestep2"] = timestep2
JSON["timestep3"] = timestep3
JSON["NumericalA"] = nA
JSON["NumericalB"] = nB
JSON["NumericalC"] = nC
JSON["AnalyticalA"] = AnalyticalA(timestep)
JSON["AnalyticalB"] = AnalyticalB(timestep)
JSON["AnalyticalC"] = AnalyticalC(timestep)
JSON['analytical_sol_A'] = AnalyticalA(T_final)
JSON['analytical_sol_B'] = AnalyticalB(T_final)
JSON['analytical_sol_C'] = AnalyticalC(T_final)


if __name__ == "__main__":

    with open("ThreeComponentDecayOutput.txt", "w") as f:
        f.write(
            f''' 
            Analytical Solution:
            After {T_final} hours...
            There is {analytical_sol_A} of Component A,
            There is {analytical_sol_B} of Component B,
            There is {analytical_sol_C} of Component C.

            Numerical solution:
            After {T_final} hours...
            There is {nA[-1]} of Component A,
            There is {nB[-1]} of Component B,
            There is {nC[-1]} of Component C.
         '''
        )
        f.close()


        with open("GraphInput.json", "w") as f:
            json.dump(JSON, f)
            f.close()