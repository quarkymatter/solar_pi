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

battery_percentage_data = []
battery_voltage_data = []

def fetch_battery_percentage():
    response = requests.get(url)
    data = response.text
    for line in data.split('\n'):
        if line.startswith('solarshed_battery_percentage'):
            percentage = float(line.split()[1])
            return percentage
    return None

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
        battery_percentage = fetch_battery_percentage()
        if battery_percentage is not None:
            timestamp = datetime.now().strftime('%H:%M')
            battery_percentage_data.append((timestamp, battery_percentage))
        else:
            print("Failed to fetch battery percentage.")
        
        battery_voltage = fetch_battery_voltage()
        if battery_voltage is not None:
            timestamp = datetime.now().strftime('%H:%M')
            battery_voltage_data.append((timestamp, battery_voltage))
        else:
            print("Failed to fetch battery voltage.")
        
        time.sleep(refresh_interval)
        

def print_battery_percentage():
    while not battery_percentage_data:
        print("No battery percentage data available yet.")
        time.sleep(refresh_interval)

    print("Battery percentage data received")

def print_battery_voltage():
    while not battery_voltage_data:
        print("No battery votlage data available yet.")
        time.sleep(refresh_interval)

    print("Battery voltage data received")    

def update_graph(i):
    timestamps, voltages = zip(*battery_voltage_data)
    ax1.clear()
    ax1.plot(timestamps, voltages)
    ax1.set_ylabel('Voltage (V)')  
    ax1.set_xlabel('Time (24-hour)')
    ax1.set_xticklabels([])  # Remove x-axis tick labels
    ax1.set_title('Battery Voltage')
    plt.xticks(rotation=0)
    
    # Update x-axis tick labels
    if battery_voltage_data:
        first_timestamp = battery_voltage_data[0][0]
        last_timestamp = battery_voltage_data[-1][0]
        ax1.set_xticks([first_timestamp, last_timestamp])
        ax1.set_xticklabels([first_timestamp, last_timestamp])

    create_battery_percentage_bar_graph()  # Update the battery percentage bar chart



# Start a thread to update the data
data_thread = Thread(target=update_data)
data_thread.daemon = True
data_thread.start()

# Start a thread to print the battery percentage
print_thread = Thread(target=print_battery_percentage)
print_thread.daemon = True
print_thread.start()

# Set the 'ggplot' style
plt.style.use('ggplot')



# Create the figure and axes for the graphs
fig = plt.figure(figsize=(7,7))
gs = gridspec.GridSpec(nrows=1, 
                       ncols=2, 
                       figure=fig, 
                       width_ratios= [3, 1],
                       height_ratios=[1],
                       wspace=0.3,
                       hspace=0.3)
                       
ax1 = fig.add_subplot(gs[0,0])
ax2 = fig.add_subplot(gs[0,1:3])

#fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 8))



# Create an animation to update the battery voltage graph
ani = animation.FuncAnimation(fig, update_graph, interval=refresh_interval*1000)




def create_battery_percentage_bar_graph():
    battery_percentage = fetch_battery_percentage()
    if battery_percentage is not None:
        ax2.clear()
        ax2.bar('Current', battery_percentage, color='#6495ED')
        ax2.set_ylim(0, 100)
	ax2.set_ylabel('
        ax2.set_title('Battery Percentage',fontsize=12)
    else:
        print("Failed to fetch battery percentage.")
	
	
create_battery_percentage_bar_graph()  # Update the battery percentage bar chart	
	

# Show the plot
#plt.tight_layout()
plt.show()


                              
