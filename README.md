# PERT Chart Generator

This project is a Python module that generates a Program Evaluation and Review Technique (PERT) chart based on input data from an Excel file.

## Description

The PERT Chart Generator reads activity data from an Excel file, including activity IDs, durations, and predecessors. It then constructs a graph representation of the activities and their dependencies, and visualizes this as a PERT chart using NetworkX and Matplotlib.

## Features

- Read activity data from Excel files
- Generate a graph representation of activities and their dependencies
- Visualize the PERT chart with labeled nodes and edges
- Display activity durations on the chart
- Command-line interface for easy usage

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```
## Usage

To generate a PERT chart, use the following command:

```bash
python main.py <path_to_excel_file>
```
Replace `<path_to_excel_file>` with the path to your Excel file containing the activity data.
