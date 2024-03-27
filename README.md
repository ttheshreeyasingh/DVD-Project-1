# DVD-Project-1 

## Overview
This project, implemented as part of the Digital VLSI Design course aims to explore the behavior of MOSFETs in digital VLSI circuits through simulation and analysis. By investigating transistor characteristics, transistor stacks, and circuit leakage, the project aims to provide valuable insights into the design and optimization of digital circuits.
Spanning multiple stages, the project progresses from characterizing individual MOSFETs to estimating leakage in complex gate-level schematics.

## Parameters
- Model Files: 45nm MGK
- Supply Voltage: 1.1V
- Temperature: 25°C

## Requirements
To execute the project, the following tools are required:
- Ngspice
- Python

## Stages

### Stage 1: MOSFET Characterization
Characterization of MOSFETs involves generating matrices of single NMOS and PMOS transistors under varying widths and supply voltages. 

### Stage 2: Transistor Stack Analysis
Stage 2 focuses on generating matrices comprising NMOS and PMOS stacks, each consisting of two transistors. By considering four input combinations (00, 01, 10, and 11) and maintaining a constant supply voltage (1.1V), intermediate node voltages are extracted.

### Stage 3: Leakage Estimation
The Final Stage involves developing a script to estimate leakage in an ISCAS 74182 circuit using matrices generated in previous stages. The script replaces 3 or 4-input gates with 2-input gates for accuracy. Additionally, the circuit netlist is designed in Ngspice for cross-verification.

## Directory Structures
- `stage_1`: Contains files related to Stage 1.
- `stage_2`: Contains files related to Stage 2.
- `stage_3`: Contains files related to leakage estimation in the ISCAS 74182 circuit.

## Team Members
- Sri Anvith Dosapati
- Sankalp S Bhat
- Shreeya Singh
- Srujana Vanka
  
--- 
