## returns and updates battery voltage & solar voltage plot as well as battery temp ##


import requests
import time
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from threading import Thread
import matplotlib.animation as animation





url = 'http://155.101.22.137:5000'
refresh_interval = 60  # seconds

battery_voltage_data = []
#solar_voltage_data = []


def fetch_voltage_data():
    response = requests.get(url)
    data = response.text
    for line in data.split('\n'):
        if line.startswith('solarshed_battery_volts'):
            battery_voltage = float(line.split()[1])
            battery_timestamp = datetime.now().strftime('%H:%M')
            battery_voltage_data.append((battery_timestamp, battery_voltage))
        #elif line.startswith('solarshed_solar_volts'):
            #solar_voltage = float(line.split()[1])
            #solar_timestamp = datetime.now().strftime('%H:%M')
            #solar_voltage_data.append((solar_timestamp, solar_voltage))


def update_data():
    while True:
        fetch_voltage_data()
        time.sleep(refresh_interval)

def update_graph(i):
    battery_timestamps, battery_voltages = zip(*battery_voltage_data)
   # solar_timestamps, solar_voltages = zip(*solar_voltage_data)

    max_voltage = max(battery_voltages)
    min_voltage = min(battery_voltages)
    upper_limit = max_voltage + 0.1  # Adding a small margin
    lower_limit = min_voltage - 0.1  # Subtracting a small margin

    ax.clear()
    ax.plot(battery_timestamps, battery_voltages)
   # ax.plot(solar_timestamps, solar_voltages, label='Solar')
    ax.plot(battery_timestamps, [upper_limit] * len(battery_timestamps), 'b--')
    ax.plot(battery_timestamps, [lower_limit] * len(battery_timestamps), 'g--')
    ax.set_ylabel('Voltage (V)')
    ax.set_xlabel('Time (HH:MM)')
    ax.set_title('Battery Voltage')
    #ax.legend()
    plt.xticks(rotation=0)
    
    if battery_voltage_data:
        first_battery_timestamp = battery_voltage_data[0][0]
        last_battery_timestamp = battery_voltage_data[-1][0]
        ax.set_xticks([first_battery_timestamp, last_battery_timestamp])
        ax.set_xticklabels([first_battery_timestamp, last_battery_timestamp])
    
   # if solar_voltage_data:
        #first_solar_timestamp = solar_voltage_data[0][0]
        #last_solar_timestamp = solar_voltage_data[-1][0]
        #ax.set_xticks([first_solar_timestamp, last_solar_timestamp])
        #ax.set_xticklabels([first_solar_timestamp, last_solar_timestamp])

    # Add labels adjacent to the lines
    ax.annotate(r'$\uparrow$' + f'{upper_limit:.2f} V', (battery_timestamps[-1], upper_limit), xytext=(5, 0), textcoords='offset points', color='blue')
    ax.annotate(r'$\downarrow$' + f'{lower_limit:.2f} V', (battery_timestamps[-1], lower_limit), xytext=(5, 0), textcoords='offset points', color='green')


# Start a thread to update the data
data_thread = Thread(target=update_data)
data_thread.daemon = True
data_thread.start()


# Temperature data

#battery_temp_data = []
#temperature = 0


response = requests.get(url)
data = response.text
#for line in data.split('\n'):
        #if line.startswith('solarshed_battery_temperature_celsius'):
                #temperature = float(line.split()[1])


# Set the 'ggplot' style
plt.style.use('ggplot')

# Create the figure and axes for the graphs
fig, ax = plt.subplots()

# Create an animation to update the voltage graph
ani = animation.FuncAnimation(fig, update_graph, interval=refresh_interval*1000, cache_frame_data=False)


# Show the plot
plt.show()
