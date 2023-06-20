### BETA /// 


# solar_pi



# Solar Charge Controller Data with Raspberry Pi Repository

This repository collects data from solar charge controllers and provides a script for retrieving and processing the data using a Raspberry Pi. The basis of this repository uses `solarshed.py` (https://github.com/corbinbs/solarshed).

## Introduction

This Solar Charge Controller Data Repository aims to gather information from Renogy solar charge controllers to monitor and analyze their performance in real-time using a Raspberry Pi network, as well as store data history.

## Features

- Collects data from Renogy solar charge controllers connected to Raspberry Pi via USB (using ethernet)

- Retrieves data through the `solarshed.py` script with minor modifications (see below)

- Enables monitoring and analysis of solar system performance using Raspberry Pi local network

## Repository Structure

- `renogy_rover.py`: Pulls data from Renogy Rover charge controller via USB - also works with Renogy Wanderer. Obtained from corbinbs/solarshed.renogg_rover.py with no modifications.

- 'server.py': Obtained from corbinbs/solarshed.server with adjusted 'SCRAPEDELAY' interval to 60 seconds.

- `get_voltage_animated.py`: Returns an animated battery voltage time series.

- `README.md`: This README file.

- `.gitignore`: Specifies the files and directories that should be ignored by Git (e.g., temporary files, logs).

## Getting Started

1. Clone this repository to your local machine:

```bash

git clone '__________'

```

2. Install the necessary dependencies. Make sure you have Python 3.x and pip installed, and then run:

```bash

pip install -r requirements.txt

```

3. If necessary, configure the `renogy_rover.py` script to communicate with your specific charge controller(s). Refer to the documentation of your charge controller to understand the configuration parameters required in the script. Default is set to Renogy Rover but works with Renogy Wanderer as well.

4. Modify the variable 'SCRAPEDELAY' in 'server.py' to your preferred scrape interval (seconds).

5. Run the `server.py` script on the Raspberry Pi through its local host ('http://ipaddress:port') to start collecting data from the charge controllers:

```bash

python server.py

```

5. The script will scrape data from controller and send to the Pi's network at the set intervals.
   

## Contributing

Contributions to this repository are welcome! If you would like to add functions or enhance the functionality of the included files, please feel free to submit a pull request.

Before submitting a pull request, please ensure that your code adheres to the repository's coding standards and is well-documented.

## License

This repository is licensed under the [MIT License](LICENSE). Feel free to modify and distribute the code as needed.

## Contact

For any inquiries or issues related to this repository, please contact Whitney at [w.osborn@utah.edu](mailto:w.osborn@utah.edu).
