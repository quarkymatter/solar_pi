# solar_pi
Solar charge controller data retrieved via Raspberry Pi network.

This repository collects data from solar charge controllers and provides a script for retrieving, storing, and processing the data in real-time using a Raspberry Pi. The basis of this repository uses `solarshed.py` - https://github.com/corbinbs/solarshed

## Hardware Setup

![image](https://github.com/quarkymatter/solar_pi/assets/132121881/f9b4f8ec-2104-494c-bd03-22f038445ad3)



## Getting Started

1. Download solar_pi zip to the RaspberryPi connected to ethernet.

2. Change working directory to /solar_pi then run the `server.py` script:

```bash

python server.py &

```

3. Verify operation by visiting http://ipaddress:5000.
4. Run led.py concurrently on the Pi to control power to the load via relay. Make suer to set the preferred upper and lower voltage limits within the script. 
5. To begin plotted display, run 'get_voltage_animated.py' on desktop computer. Voltage will update on the graph every 60 seconds.


![battery_voltage_cycle](https://github.com/quarkymatter/solar_pi/assets/132121881/6a0b6118-3742-498a-8d6f-c3b994b40360)

## Contact

For any inquiries or issues related to this repository, please contact Whitney at [w.osborn@utah.edu](mailto:w.osborn@utah.edu).
