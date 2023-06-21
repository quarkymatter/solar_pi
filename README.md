### \\\ BETA /// 


# solar_pi



# Solar Charge Controller Data with Raspberry Pi

This repository collects data from solar charge controllers and provides a script for retrieving, storing, and processing the data in real-time using a Raspberry Pi. The basis of this repository uses `solarshed.py` - https://github.com/corbinbs/solarshed


## Features

- Collects data from Renogy solar charge controllers connected to Raspberry Pi via USB (using ethernet)

- Retrieves data through the `solarshed.py` script with minor modifications (see below)

- Enables monitoring and analysis of solar system performance using Raspberry Pi local network

## Repository Structure

- `renogy_rover.py`: Pulls data from Renogy Rover charge controller via USB - also works with Renogy Wanderer. Obtained from corbinbs/solarshed.renogg_rover.py with no modifications.

- `server.py`: Obtained from corbinbs/solarshed.server with adjusted 'SCRAPEDELAY' interval to 60 seconds. Currently written for 155.101.22.137.

- `get_voltage_animated.py`: Returns an animated battery voltage time series.

- `README.md`: This README file.


## Getting Started

Download solar_pi zip to your computer, then copy the extracted zip to the Raspberry Pi using:

```bash

scp -r /path/to/local/folder pi@ipaddress:/home/pi/my_folder

```
Ex. 'scp -r /home/whitney/solar_pi tamember@155.101.22.137:/home/tamember/solar_pi'

Change working directory to /solar_pi then run the `server.py` script:

```bash

python -m solar_pi.server

```

   

## Contributing

Contributions to this repository are welcome! If you would like to add functions or enhance the functionality of the included files, please feel free to submit a pull request.

Before submitting a pull request, please ensure that your code adheres to the repository's coding standards and is well-documented.

## License

This repository is licensed under the [MIT License](LICENSE). Feel free to modify and distribute the code as needed.

## Contact

For any inquiries or issues related to this repository, please contact Whitney at [w.osborn@utah.edu](mailto:w.osborn@utah.edu).
