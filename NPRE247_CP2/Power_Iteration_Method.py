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
    Inscattering_matrix = np.zeros((len(scat_data),len(scat_data[0])))
    for i in range(len(scat_data)):
        for j in range(len(scat_data.T)):
            if i ==j:
                continue
            else:
                Inscattering_matrix[j,i] = scat_data[i,j]
    return Inscattering_matrix

def Outscattering_matrix(scat_data):
    Outscattering_matrix = np.zeros((len(scat_data),len(scat_data[0])))
    for i in range(-1,len(scat_data)-1):
        Outscattering_matrix[i,i] = scat_data[i,i+1]
    return Outscattering_matrix



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


# Create matricies
k = np.zeros(100)
k[0] = 1
flux = np.zeros((len(scat_data),100))
flux[:,0] = np.ones(len(scat_data))

fission_matrix = Create_fission_matrix(group_data)
absorbtion_matrix = Create_absorbtion_matrix(group_data)
outscattering_matrix = Outscattering_matrix(scat_data)
inscattering_matrix = Inscattering_matrix(scat_data)

mitigation_matrix = absorbtion_matrix + outscattering_matrix - inscattering_matrix

b_matrix = la.inv(mitigation_matrix) @ fission_matrix

eigenvalues, eigenvectors = la.eig(b_matrix)


# Power Iteration
for i in range(99):
    flux[:,i+1] = (b_matrix @ flux[:,i]) / la.norm(b_matrix @ flux[:,i])
for i in range(99):
    k[i+1] = ((b_matrix @ flux[:,i+1]).T @ flux[:,i+1])/(flux[:,i+1].T @ flux[:,i+1])


if __name__ == "__main__":