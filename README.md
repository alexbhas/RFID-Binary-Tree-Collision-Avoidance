# RFID-Collision-Avoidance

This repository contains a Python simulation for the COMP 4203 project, which replicates the work of Cheng and Jin's research paper, [Analysis and Simulation of RFID Anti-collision Algorithms](https://ieeexplore.ieee.org/abstract/document/4195229). The purpose of the project is to compare the performance of the Binary Tree RFID anti-collision algorithm against other anti-collision methods, specifically focusing on the effectiveness of the Binary Tree algorithm approach to tag identification and collision avoidance by evaluating the number of slots taken to differentiate all tags.

## Overview

RFID (Radio Frequency Identification) is a wireless system that leverages radio frequency for the identification of tags using a designated reader. This project implements two anti-collision algorithms, the Gen 1 protocol and the Binary Tree protocol. The simulations were run with varying numbers of tags, and the results were compared to the results from Cheng and Jin's research paper.

## Results

The Binary Tree protocol takes fewer slots, on average, to identify up to 2000 tags compared to the Gen 1 protocol. It was found that the Binary Tree protocol is more efficient overall relative to slot usage.

## Implementation

This project simulates and compares the performance of two RFID anti-collision algorithms: Gen 1 protocol and Binary Tree protocol. The code is organized into several files, with main.py running the simulations, plotter.py handling the visualization using matplotlib, and reader.py implementing the core algorithms. The simulation process calculates the number of slots needed for successful tag identification for various sample sizes, and the results are graphed using the Plot and MultiPlot classes. The GenOneTagReader and BinaryTagReader subclasses of BaseTagReader in reader.py manage tag collisions, while the run_simulation() function in simulation.py simulates tag-reader communication. Finally, the simulation results are plotted alongside the research paper data for comparison.

## Dependencies

- Python 3
- numpy
- matplotlib

## How to Run

To run the simulation, simply run the following command:
```python3 src```

