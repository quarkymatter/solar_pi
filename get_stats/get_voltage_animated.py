# Update 2023 June 23 - removed battery percentage


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



def fetch_battery_voltage():
    response = requests.get(url)
    data = response.text
    for line in data.split('\n'):
        if line.startswith('solarshed_battery_volts'):
            voltage = float(line.split()[1])
            return voltage
    return None

def update_data():
    while True:
        battery_voltage = fetch_battery_voltage()
        if battery_voltage is not None:
            timestamp = datetime.now().strftime('%H:%M')
            battery_voltage_data.append((timestamp, battery_voltage))
        else:
            print("Failed to fetch battery voltage.")
        
        time.sleep(refresh_interval)
        



def print_battery_voltage():
    while not battery_voltage_data:
        print("No battery votlage data available yet.")
        time.sleep(refresh_interval)

    print("Battery voltage data received")    

def update_graph(i):
    timestamps, voltages = zip(*battery_voltage_data)
    ax.clear()
    ax.plot(timestamps, voltages)
    ax.set_ylabel('Voltage (V)')  
    ax.set_xlabel('Time (HH:MM)')
    ax.set_xticklabels([])  # Remove x-axis tick labels
    ax.set_title('Battery Voltage')
    plt.xticks(rotation=0)
    
    # Update x-axis tick labels
    if battery_voltage_data:
        first_timestamp = battery_voltage_data[0][0]
        last_timestamp = battery_voltage_data[-1][0]
        ax.set_xticks([first_timestamp, last_timestamp])
        ax.set_xticklabels([first_timestamp, last_timestamp])

   


# Start a thread to update the data
data_thread = Thread(target=update_data)
data_thread.daemon = True
data_thread.start()



# Set the 'ggplot' style
plt.style.use('ggplot')



# Create the figure and axes for the graphs
fig, ax = plt.subplots()



# Create an animation to update the battery voltage graph
ani = animation.FuncAnimation(fig, update_graph, interval=refresh_interval*1000,cache_frame_data=False)


# Show the plot
plt.show()
