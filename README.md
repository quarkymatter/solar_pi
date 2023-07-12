# solar_pi
Solar charge controller data retrieved via Raspberry Pi network.
### \\\ BETA /// 


# solar_pi



# Solar Charge Controller Data with Raspberry Pi

This repository collects data from solar charge controllers and provides a script for retrieving, storing, and processing the data in real-time using a Raspberry Pi. The basis of this repository uses `solarshed.py` - https://github.com/corbinbs/solarshed

![image](https://github.com/quarkymatter/solar_pi/assets/132121881/f9b4f8ec-2104-494c-bd03-22f038445ad3)


## Repository Structure (currently written for 155.101.22.137)

- `renogy_rover.py`: Pulls data from Renogy Rover charge controller via USB - also works with Renogy Wanderer. Obtained from corbinbs/solarshed.renogg_rover.py with no modifications.

- `server.py`: Obtained from corbinbs/solarshed.server with adjusted 'SCRAPEDELAY' interval to 60 seconds.

- `get_voltage_animated.py`: Returns an animated battery voltage time series.

- `README.md`: This README file.


## Getting Started

1. Download solar_pi zip to your computer, then copy the extracted zip to the Raspberry Pi using:

```bash

scp -r /path/to/local/folder pi@ipaddress:/home/pi/my_folder

```

example. 'scp -r /home/whitney/solar_pi tamember@155.101.22.137:/home/tamember/solar_pi'




2. Change working directory to /solar_pi then run the `server.py` script:

```bash

python -m solar_pi.server &

```

3. Verify that the Pi is scraping data by visiting http://157.101.22.137:5000.
4. To begin data displays, change to the appropriate directory on current computer and run 'get_voltage_animated.py'. Data should update on the graph every 60 seconds.


![battery_voltage_cycle](https://github.com/quarkymatter/solar_pi/assets/132121881/6a0b6118-3742-498a-8d6f-c3b994b40360)

## Contact

For any inquiries or issues related to this repository, please contact Whitney at [w.osborn@utah.edu](mailto:w.osborn@utah.edu).
