# Stage 3: Leakage Estimation

## Introduction
This stage of the project focuses on the estimation of leakage current in digital circuits using both single transistors and transistor stacks. The leakage estimation is performed through Python scripts and verified by simulating the circuit in NGSPICE and observing the output.

## Files and Scripts
- `circuit_leakage.py`: Python script for leakage estimation using both single transistors and transistor stacks.
- `ISCAS_74182.net`: Netlist file for the ISCAS 74182 circuit used in NGSPICE simulation.
- `Gate_Simulation.txt`: Output file generated from NGSPICE simulation.

## Execution Steps
1. **Leakage Estimation using Python**:
   - Execute the Python script `circuit_leakage.py`.
   - Provide input values as required.
   - The script will estimate leakage currents using both single transistors and transistor stacks.

2. **NGSPICE Simulation for Cross Verification**:
   - Run NGSPICE simulation using the netlist file `ISCAS_74182.net`:
     ```
     ngspice ISCAS_74182.net > Gate_Simulation.txt
     ```
   - Observe the output generated in `Gate_Simulation.txt` for further analysis.

## Conclusion
This stage provides a comprehensive approach to leakage current estimation in digital circuits. By combining Python scripts for estimation and NGSPICE simulation for cross-verification, a thorough understanding of leakage currents and their impact on circuit behavior is achieved.

---