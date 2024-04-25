This is the code for the second computer project for NPRE247. This code takes in group data (absorbtion cross sections, fission cross sections, and X probabilities) and scattering data (scattering cross sections from each to group to each other group) to return the fission matrix, mitigation matrix, inscattering and outscattering matricies, the "b" matrix, eigenvalues and eigenvectors of that matrix, flux and k as it is iterated through power iteration (uses inital flux, [1,1] and inital k, 1) over two iterations, and the final k value and flux array resulting from that iteration.

The code is ran in terminal by running: python3 .\Power_Iteration_Method.py [group data input file] [scattering data input file]


For two group using the provided inital data, it looks like: 

python3 .\Power_Iteration_Method.py .\Two-group_data.0000 '.\Two group scattering.0000'


For eight group using the provided inital data, it looks like: 

python3 .\Power_Iteration_Method.py .\Eight_group_data.0000 .\Eight_group_scattering.000


The group data input file should be structured so that each line representes a different group and each entry (seperated by a space) should be: absorbtion macroscopic cross section, average neutrons per fission multiplied by macroscopic fission cross section, and X probability value in that order. It should look like this:

[Abs Xs] [v*Fis Xs] [X value]     (all values for group 1)

[Abs Xs] [v*Fis Xs] [X value]     (all values for group 2)

...

The scattering data should be formatted so that each entry across a row (separated by a space) representes where a neutron scatters from and each entry across a column
(separated by a new line) representes where the neutron scatters to. The entries them selves represent the scattering cross sections from their respective column to
their respective row. It should look like this:

[Scat Xs (1 to 1)] [Scat Xs (2 to 1)] ...

[Scat Xs (1 to 2)] [Scat Xs (2 to 2)] ...

...
