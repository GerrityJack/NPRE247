Run ThreeComponentDecayChain.py with an input file (ThreeComponentDecayChainInput.txt). In the terminal, it looks like this:
python3 ThreeComponentDecayChain.py ThreeComponentDecayChainInput.txt

The input file should contain:
the two half lives (half),
the inital number of each isotope (N_0),
the time after which isotope quantities are measured (t_final)
and the time incremented over (deltat)

The input file should be structured like so:
halfA (in hours)
halfB (in hours)
N_A0
N_B0
N_C0
deltat (in hours)
T_final (in hours)

The program will return the following results to an output file:

ThreeComponentDecayOutput.txt (text file)
    Numerical and Analytical solutions

GraphInput.json (JSON File) 
    File to be used as input to plot graph with PlotDecayChain Function:
        python3 PlotDecayChain.py GraphInput.json 

    Outputs:
        Three Component Decay Chain Graph.png
            Graph of Coarse, Medium and Fine Numerical Solutions for Isotopes A, B, and C along with Analytical Solution

        Isotope B Graph.png
            Graph of Coarse, Medium and Fine Numerical Solutions for Isotope B along with Analytical Solution

        Time at which Isotope B Reaches a Maxium Graph.png
            Graph of Fine Numerical Solutions along with Sum of All Isotopes at Every Time Value

        Numerical decays with Total Isotope Count.png
            Graph Comparing the Effects of Different Changes in Time with the Time at which Isotope B Reaches a Maximum
