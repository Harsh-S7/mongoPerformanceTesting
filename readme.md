# Group 2 - Characterising the Performance of MongoDB: A NoSQL Database

## Overview

This repository contains the Python scripts for benchmarking CRUD operations in MongoDB as part of the SENG 533 course project by Group 2. The objective is to analyze and characterize the performance of MongoDB, a NoSQL database, under various conditions and operations.

## Files

The repository includes the following scripts:

- `create.py`: Script to perform create operations in MongoDB.
- `read.py`: Script to perform read operations.
- `update.py`: Script to perform update operations.
- `delete.py`: Script to perform delete operations.

Each script is responsible for interacting with the MongoDB database and performing specific CRUD operations to measure performance metrics.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- MongoDB server (local or remote)

### Installing Dependencies

To install the required Python libraries, run:

```bash
pip install -r requirements.txt
```

Ensure that MongoDB is correctly installed and running on your system or accessible remotely. Configuration details might need to be adjusted in the scripts according to your setup.

### Configuration

Modify the MongoDB connection settings in each script to match your environment:

- Host (Local host is used as a template)
- Port (27017 is used as a a template)
- Authentication details (if any)

## Usage

To run any of the scripts, use the following command:

```bash
python <script_name>.py
```

Replace `<script_name>` with `create`, `read`, `update`, or `delete` depending on the operation you want to perform.

## Results and Reporting

The scripts will output performance metrics such as execution time and throughput. The raw results can be vieiwed on this [google sheet](https://docs.google.com/spreadsheets/d/1_ec0n4S2D6-A7Reffu53Ars_6O_95Jx3JRD73n5D9n0/edit?usp=sharing) For detailed analysis and report generation, refer to the accompanying project report: _Characterising the Performance of MongoDB: A NoSQL Database_.

## Contributing

Contributions to this project are welcome. Please follow the standard fork-and-pull request workflow.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Course instructors and TAs of SENG 533
- MongoDB documentation and community resources
