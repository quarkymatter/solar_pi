import requests
import time


url = 'http://155.101.22.137:5000'
refresh_interval = 500  # seconds


battery_temp_data = []
temperature = 0


response = requests.get(url)
data = response.text
for line in data.split('\n'):
        if line.startswith('solarshed_battery_temperature_celsius'):
                temperature = float(line.split()[1])


print('temperature,'°C')

