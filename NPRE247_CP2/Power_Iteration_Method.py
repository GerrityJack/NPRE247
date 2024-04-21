# Import Libraries

import sys
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import json

# Deine Functions

def Create_fission_matrix(group_data):
    dis = len(group_data)
    fission_matrix = np.ones((dis,dis))
    for i in range(dis):
        for j in range(dis):
            fission_matrix[i,j] = group_data[i,2] * group_data[i,1]
    return fission_matrix

def Create_absorbtion_matrix(group_data):
    dis = len(group_data)
    absorbtion_matrix = np.zeros((dis,dis))
    for i in range(dis):
        absorbtion_matrix[i][i] = group_data[i,0]
    return absorbtion_matrix

def Inscattering_matrix(scat_data):
    
    for i in range(scat_data):
        for j in range(scat_data.T):
            if i ==j:
                continue

# Parse Input Data

f = open(sys.argv[1], "r")
Input = f.readlines()
f.close()

group_data = np.ones((len(Input),3))
for c, i in enumerate(Input):
    group = Input[c].split(" ")
    group_data[c,0] = float(group[0])
    group_data[c,1] = float(group[1])
    group_data[c,2] = float(group[2])


g = open(sys.argv[2], "r")
Input2 = g.readlines()
g.close()


scat_list = []
for i in range(len(Input2)):
    scat_list.append(Input2[i].split(" "))
scat_data = np.zeros((len(Input),len(scat_list[0])))
for i in range(len(scat_list)):
    for j in range(len(scat_list[0])):
        scat_data[i,j] = float(scat_list[i][j])





if __name__ == "__main__":