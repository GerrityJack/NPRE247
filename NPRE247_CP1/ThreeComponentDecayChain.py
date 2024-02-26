# Import Libraries

import sys
import numpy as np
import matplotlib.pyplot as plt
import json

# Deine Functions

def AnalyticalA(T):
    return N_A0 * np.exp(-lambdaA*T)

def AnalyticalB(T):
    return (lambdaA/(lambdaB-lambdaA))*N_A0*(np.exp(-lambdaA*T)-np.exp(-lambdaB*T)) + N_B0* np.exp(-lambdaB*T)

def AnalyticalC(T):
    return (N_A0-N_A0* np.exp(-lambdaA*T)-((lambdaA/(lambdaB-lambdaA))*N_A0*(np.exp(-lambdaA*T)-np.exp(-lambdaB*T)) + N_B0* np.exp(-lambdaB*T)))- + N_C0


# Open file and read to associated variables

f = open(sys.argv[1], "r")
Input = f.readlines()
f.close()

halfA = float(Input[0])
halfB = float(Input[1])
N_A0 = float(Input[2])
N_B0 = float(Input[3])
N_C0 = float(Input[4])
deltat = float(Input[5])
T_final = float(Input[6])

# Define Variables

lambdaA = np.log(2)/halfA
lambdaB = np.log(2)/halfB

analytical_sol_A = AnalyticalA(T_final)
analytical_sol_B = AnalyticalB(T_final)
analytical_sol_C = AnalyticalC(T_final)

timestep = np.linspace(0,T_final,int(T_final/(deltat)))
timestep2 = np.linspace(0,T_final,int(T_final/(deltat/2)))
timestep3 = np.linspace(0,T_final,int(T_final/(deltat/4)))

# Set up Numerical Analysis Matricies

nA = np.zeros(int(T_final/deltat))
nA[0] = N_A0
nAm = np.zeros(int(T_final/(deltat/2)))
nAm[0] = N_A0
nAf = np.zeros(int(T_final/(deltat/4)))
nAf[0] = N_A0

nB = np.zeros(int(T_final/deltat))
nB[0] = N_B0
nBm = np.zeros(int(T_final/(deltat/2)))
nBm[0] = N_B0
nBf = np.zeros(int(T_final/(deltat/4)))
nBf[0] = N_B0

nC = np.zeros(int(T_final/deltat))
nC[0] = N_C0
nCm = np.zeros(int(T_final/(deltat/2)))
nCm[0] = N_C0
nCf = np.zeros(int(T_final/(deltat/4)))
nCf[0] = N_C0

# Fill in nA, nB, nC

for i in range(len(nA)-1):
    nA[i+1] = -lambdaA * nA[i] * deltat + nA[i]
for i in range(len(nAm)-1):
    nAm[i+1] = -lambdaA * nAm[i] * (deltat/2) + nAm[i]
for i in range(len(nAf)-1):
    nAf[i+1] = -lambdaA * nAf[i] * (deltat/4) + nAf[i]

for i in range(len(nB)-1):
    nB[i+1] = lambdaA*nA[i] * deltat - lambdaB*nB[i] * deltat + nB[i]
for i in range(len(nBm)-1):
    nBm[i+1] = lambdaA*nAm[i] * (deltat/2) - lambdaB*nBm[i] * (deltat/2) + nBm[i]
for i in range(len(nBf)-1):
    nBf[i+1] = lambdaA*nAf[i] * (deltat/4) - lambdaB*nBf[i] * (deltat/4) + nBf[i]

for i in range(len(nC)-1):
    nC[i+1] = lambdaB*nB[i] * deltat + nC[i]
for i in range(len(nCm)-1):
    nCm[i+1] = lambdaB*nBm[i] * (deltat/2) + nCm[i]
for i in range(len(nCf)-1):
    nCf[i+1] = lambdaB*nBf[i] * (deltat/4) + nCf[i]


# Create Dictionary to Read to JSON

JSON = {}
JSON["timestep"] = list(timestep)
JSON["timestep2"] = list(timestep2)
JSON["timestep3"] = list(timestep3)
JSON["NumericalA"] = list(nA)
JSON["NumericalB"] = list(nB)
JSON["NumericalC"] = list(nC)
JSON["NumericalAm"] = list(nAm)
JSON["NumericalBm"] = list(nBm)
JSON["NumericalCm"] = list(nCm)
JSON["NumericalAf"] = list(nAf)
JSON["NumericalBf"] = list(nBf)
JSON["NumericalCf"] = list(nCf)
JSON["AnalyticalA"] = list(AnalyticalA(timestep))
JSON["AnalyticalB"] = list(AnalyticalB(timestep))
JSON["AnalyticalC"] = list(AnalyticalC(timestep))
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