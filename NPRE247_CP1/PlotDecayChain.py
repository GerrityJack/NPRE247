import json
import numpy as np
import matplotlib as plt
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
AnalyticalA = JSON["AnalyticalA"] 
AnalyticalB = JSON["AnalyticalB"]
AnalyticalC = JSON["AnalyticalC"]


# Plot Analytical Solutions

plt.plot(timestep,AnalyticalA,'k',label = 'Analytical A')
plt.plot(timestep,AnalyticalB,'b',label = 'Analytical B')
plt.plot(timestep,AnalyticalC,'g',label = 'Analytical C')

# Plot Numerical Solutions

plt.plot(timestep,nA,'ko',label = 'Numerical A (Course)')
plt.plot(timestep,nB,'bo',label = 'Numerical B (Cource)')
plt.plot(timestep,nC,'go',label = 'Numerical C (Cource)')
plt.plot(timestep,nA,'k.',label = 'Numerical A (Medium)')
plt.plot(timestep,nB,'b.',label = 'Numerical B (Medium)')
plt.plot(timestep,nC,'g.',label = 'Numerical C (Medium)')
plt.plot(timestep,nA,'k:',label = 'Numerical A (Fine)')
plt.plot(timestep,nB,'b:',label = 'Numerical B (Fine)')
plt.plot(timestep,nC,'g:',label = 'Numerical C (Fine)')



if __name__ == "__main__":

    plt.xlabel('Time (Hours)')
    plt.ylabel('Quanitiy of Component')
    plt.title('Three Component Decay Chain Calculated Numerically and Analytically')
    plt.legend()
    plt.ioff()
    plt.ion()
    plt.savefig('Three Component Decay Chain Graph')