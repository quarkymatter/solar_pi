import requests
import time
from datetime import datetime
import matplotlib.pyplot as plt
from threading import Thread
import matplotlib.animation as animation

url = 'http://155.101.22.137:5000' # address for the raspi 
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
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            battery_voltage_data.append((timestamp, battery_voltage))
            #print(f"[{timestamp}] Battery Voltage: {battery_voltage} V") #uncomment to print
        else:
            print("Failed to fetch battery voltage.")
        time.sleep(refresh_interval)
        

def update_graph(i):
    timestamps, voltages = zip(*battery_voltage_data)
    ax.clear()
    ax.plot(timestamps, voltages)
    ax.set_ylabel('Battery Voltage (V)')  
    ax.set_xticklabels([])  # Remove x-axis tick labels
    ax.set_title('Battery Voltage Time Series')
    plt.xticks(rotation=45)

# Start a thread to update the data
data_thread = Thread(target=update_data)
data_thread.daemon = True
data_thread.start()

# Create the figure and axis for the graph
fig, ax = plt.subplots()

# Create an animation to update the graph
ani = animation.FuncAnimation(fig, update_graph, interval=refresh_interval*1000)

# Show the plot
plt.show()

