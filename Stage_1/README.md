# DVD-Project-1 Stage 1

## Overview
The objective of DVD-Project-1 Stage 1 is to characterize MOSFET behavior using Ngspice. This stage involves analyzing the performance of MOSFETs under varying transistor widths and supply voltages.

## Requirements
To execute the simulations for Stage 1, ensure you have the following tools installed:
- Ngspice
- Python

## Instructions to Run

1. Navigate to the NMOS or PMOS directory based on the type of MOSFET you want to characterize:
   ```bash
   cd NMOS_on
   ```
   or
    ```bash
    cd PMOS_on
    ```
    or
    ```bash
    cd NMOS_off
    ```
    or
    ```bash
    cd PMOS_off
    ```

2. Run the Python script to generate netlist files and run Ngspice simulations:
   ```bash
   python nmos_on_script.py
   ```
    or
    ```bash
    python pmos_on_script.py
    ```
    or
    ```bash
    python nmos_off_script.py
    ```
    or
    ```bash
    python pmos_off_script.py
    ```

5. After the simulations are completed, you can find the output files in the `simulation_results` directory.

## Directory Structure
- `NMOS_on` and `NMOS_off` directories: Contains netlist templates for NMOS transistor in ON and OFF states with varying widths.
- `PMOS_on` and `PMOS_off` directories: Contains netlist templates for PMOS transistor in ON and OFF states with varying widths.
    - `netlists/`: Contains netlist files generated for different transistor widths.
    - `simulation_results/`: Contains output files generated by Ngspice simulations for varying widths.

---
