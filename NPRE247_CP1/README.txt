Run ThreeComponentDecayChain.py with input ThreeComponentDecayChainInput.txt. In the terminal, it looks like this:
python3 ThreeComponentDecayChain.py ThreeComponentDecayChainInput.txt

The input file should contain:
the two half lives (half),
the inital number of each isotope (N_0),
the time after which isotope quantities are measured (t_final)
and the time incremented over (deltat)

The input file should be structured like so:
halfA
halfB
N_A0
N_B0
N_C0
deltat
T_final

The program will return the following results to an output file:

ThreeComponentDecayOutput.txt (text file) - Numerical and Analytical solutions
GraphInput.json (JSON File) - File to be used as input to plot graph with PlotDecayChain Function:
    python3 PlotDecayChain.py GraphInput.json 
--> Will output graph with course, medium, and fine numerical solutions as well as Analytical solutions