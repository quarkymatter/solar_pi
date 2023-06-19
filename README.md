### BETA README///FORMATTING PURPOSES ONLY


# solar_pi



# University of Utah Solar Charge Controller Data Repository

This repository collects data from solar charge controllers and provides a script for retrieving and processing the data. The basis of this repository is the `solarshed.py` script.

## Introduction

The University of Utah Solar Charge Controller Data Repository aims to gather information from various solar charge controllers to monitor and analyze their performance. By collecting data from these devices, researchers and enthusiasts can gain insights into solar energy generation and optimize the performance of solar systems.

## Features

- Collects data from solar charge controllers

- Retrieves data through the `solarshed.py` script with minor modifications 

- Provides a simple and extensible framework for adding support for different charge controller models

- Enables monitoring and analysis of solar system performance using Raspberry Pi local network

## Repository Structure

The repository has the following structure:

```

.

├── solarshed.py

├── data/

│   ├── controller1/

│   │   ├── 2023-06-01.csv

│   │   ├── 2023-06-02.csv

│   │   └── ...

│   ├── controller2/

│   │   ├── 2023-06-01.csv

│   │   ├── 2023-06-02.csv

│   │   └── ...

│   └── ...

├── README.md

└── .gitignore

```

- `solarshed.py`: The main script responsible for collecting data from the charge controllers.

- `data/`: A directory containing subdirectories for each charge controller.

- `controllerX/`: A directory for each charge controller, storing CSV files containing the data collected for each day.

- `README.md`: This README file.

- `.gitignore`: Specifies the files and directories that should be ignored by Git (e.g., temporary files, logs).

## Getting Started

To collect data from solar charge controllers and retrieve the data using the `solarshed.py` script, follow these steps:

1. Clone this repository to your local machine:

```bash

git clone https://github.com/university-of-utah/solar-charge-controller-data.git

```

2. Install the necessary dependencies. Make sure you have Python 3.x and pip installed, and then run:

```bash

pip install -r requirements.txt

```

3. Configure the `solarshed.py` script to communicate with your specific charge controller(s). Refer to the documentation of your charge controller to understand the configuration parameters required in the script.

4. Run the `solarshed.py` script to start collecting data from the charge controllers:

```bash

python solarshed.py

```

5. The script will create a CSV file for each charge controller in the `data/controllerX/` directory, with the filename corresponding to the current date. The collected data will be stored in these files.

## Contributing

Contributions to this repository are welcome! If you would like to add support for additional charge controller models or enhance the functionality of the `solarshed.py` script, please feel free to submit a pull request.

Before submitting a pull request, please ensure that your code adheres to the repository's coding standards and is well-documented.

## License

This repository is licensed under the [MIT License](LICENSE). Feel free to modify and distribute the code as needed.

## Contact

For any inquiries or issues related to this repository, please contact Whitney at [w.osborn@utah.edu](mailto:w.osborn@utah.edu).
