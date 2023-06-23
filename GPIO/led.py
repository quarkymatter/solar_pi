from gpiozero import LED
import requests
import time

# Set up the LED
led = LED(17)  # Change the GPIO pin number as per setup

# Define upper and lower limits 
upper_voltage = 13.5
lower_voltage = 12.0

# Function to fetch the battery voltage from the data source
def fetch_battery_voltage():
    response = requests.get(url)  # Replace 'url' with the actual URL
    data = response.text
    for line in data.split('\n'):
        if line.startswith('solarshed_battery_volts'):
            voltage = float(line.split()[1])
            return voltage
    return None

# Function to check the voltage and control the LED
def check_voltage():
    voltage = fetch_battery_voltage()
    if voltage is not None:
        if lower_voltage <= voltage <= upper_voltage:
            led.on()
        else:
            led.off()

# Start refresh loop
while True:
    check_voltage()
    time.sleep(60)  # Refresh interval of 60 seconds
