from gpiozero import LED
import requests
import time

# Set up the LED
led = LED(17)  # Change the GPIO pin number as per setup
url = 'http://155.101.22.137:5000'

# Define upper and lower limits 
upper_voltage = 14.2
lower_voltage = 12.8

# Function to fetch the battery voltage from the data source
def fetch_battery_voltage():
    response = requests.get(url)  # Replace as necessary
    data = response.text
    for line in data.split('\n'):
        if line.startswith('solarshed_battery_volts'):
            voltage = float(line.split()[1])
            return voltage
    return None


def check_voltage():
    voltage = fetch_battery_voltage()
    if voltage is not None:
        if lower_voltage >= voltage:
            led.off()
            print('OFF, V = ', voltage)
        else if upper_voltage <= voltage:
            led.on()
            print('ON, V = ', voltage)


# Start refresh loop
while True:
    check_voltage()
    time.sleep(60)  # Refresh interval of 60 seconds
