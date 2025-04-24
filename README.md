# Documentation

by Hailing Jia (h.jia@sron.nl)

2025-04-24

**Maximin Latin Hypercube Sampling** is used to create a parameter combination design that spans the N‐dimensional uncertain parameter space. 

1. Sepcify parameter names, their minimum and maximum values, and the desired distribution of samples in `parameters_range_list.txt`. 

2. Run `LHS.py` to generate the parameter cmobination design and write the result to PPE_values.txt/PPE_values.csv according to the parameters you have set in the parameters_range_list.txt file.

    ```shell
    $ python LHS.py
    ```
    Then, you will be asked to specify number of simulations you wish to perform, and whether you want to write to `PPE_values.txt`/`PPE_values.csv`, which is a naccesary input file for the PPE workflow.