import json
import numpy as np
import matplotlib.pyplot as plt
import sys


f = open(sys.argv[1],'r')
JSON = json.load(f)
f.close()

timestep = JSON["timestep"]
timestep2 = JSON["timestep2"]
timestep3 = JSON["timestep3"]
nA = JSON["NumericalA"]
nB = JSON["NumericalB"]
nC = JSON["NumericalC"]
nAm = JSON["NumericalAm"]
nBm = JSON["NumericalBm"]
nCm = JSON["NumericalCm"]
nAf = JSON["NumericalAf"]
nBf = JSON["NumericalBf"]
nCf = JSON["NumericalCf"]
AnalyticalA = JSON["AnalyticalA"] 
AnalyticalB = JSON["AnalyticalB"]
AnalyticalC = JSON["AnalyticalC"]
MaxB = JSON['MaxB']
changing_deltat = JSON['changing_deltat']
B_value = JSON['B_value']
timeline = JSON['timeline']


# Plot Analytical Solutions

plt.plot(timestep,AnalyticalA,'k',label = 'Analytical A')
plt.plot(timestep,AnalyticalB,'b',label = 'Analytical B')
plt.plot(timestep,AnalyticalC,'g',label = 'Analytical C')

# Plot Numerical Solutions

plt.plot(timestep,nA,'ko',label = 'Numerical A (Coarse)')
plt.plot(timestep,nB,'bo',label = 'Numerical B (Coarse)')
plt.plot(timestep,nC,'go',label = 'Numerical C (Coarse)')
plt.plot(timestep2,nAm,'k.',label = 'Numerical A (Medium)')
plt.plot(timestep2,nBm,'b.',label = 'Numerical B (Medium)')
plt.plot(timestep2,nCm,'g.',label = 'Numerical C (Medium)')
plt.plot(timestep3,nAf,'k:',label = 'Numerical A (Fine)')
plt.plot(timestep3,nBf,'b:',label = 'Numerical B (Fine)')
plt.plot(timestep3,nCf,'g:',label = 'Numerical C (Fine)')



if __name__ == "__main__":

    plt.xlabel('Time (Hours)')
    plt.ylabel('Quanitiy of Component')
    plt.title('Three Component Decay Chain Calculated Numerically and Analytically')
    plt.legend(fontsize="8")
    plt.ioff()
    plt.ion()
    plt.savefig('Three Component Decay Chain Graph')

total = np.zeros(len(timestep3))
for i in range(len(total)):
    total[i] = nAf[i] + nBf[i] + nCf[i]

plt.clf()
plt.plot(timestep3,total,'r',label = 'Total of all isotopes')
plt.plot(timestep3,nAf,'k:',label = 'Numerical A')
plt.plot(timestep3,nBf,'b:',label = 'Numerical B')
plt.plot(timestep3,nCf,'g:',label = 'Numerical C')

if __name__ == "__main__":
    plt.xlabel('Time (Hours)')
    plt.ylabel('Quanitiy of Component')
    plt.title('Three Component Decay Chain Calculated Numerically with Total')
    plt.legend(fontsize="8")
    plt.ioff()
    plt.ion()
    plt.savefig('Numerical decays with Total Isotope Count')

plt.clf()
plt.plot(changing_deltat, MaxB,'.', color="orange", label = 'Numerical Solutions for Different Changes in Time')
plt.plot(changing_deltat, timeline,'b', label = 'Empirical Solution')

if __name__ == "__main__":
    plt.xlabel('Inverse Change in Time (hours^-1)')
    plt.ylabel('Time at which Maxium of Isotope B Occurs')
    plt.title('Changing Time at which Isotope B Reaches a Maxium')
    plt.legend(fontsize="8")
    plt.xscale('log')
    plt.ioff()
    plt.ion()
    plt.savefig('Time at which Isotope B Reaches a Maxium Graph')