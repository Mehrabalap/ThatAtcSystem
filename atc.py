import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab
from tkinter import filedialog
import tkintermapview
import random
import requests
import datetime
import json
print('hello')
flights = {}

# create tkinter window
root_tk = tk.Tk()
root_tk.geometry(f"{1000}x{700}")
root_tk.title("THE M A P")

entry = None
flight_list1 = None

flight_list = None


# Create a function to open the button window
def open_button_window():
    global entry_flight_code, entry_aircraft_reg, entry_aircraft_name, entry_arrival, entry_destination, entry_priority, entry_time_in, entry_speed, flight_list1

    # Create a new tkinter window for the buttons
    button_window = tk.Toplevel(root_tk)
    button_window.title("Button Window")

    # Original Buttons - Placed side by side horizontally
    button_1 = tk.Button(button_window, text='The Magical Science thingamajig', fg='black', bg='yellow', command=TheMagicSchoolBus)
    button_2 = tk.Button(button_window, text='Bring My Limo', fg='lime', bg='green', command=BringDaLimo)
    entry = tk.Entry(button_window)
    save_button = tk.Button(button_window, text='Save Map View', fg='black', bg='cyan', command=save_map_view)
    
    satnav = tk.Button(button_window, text='Satellite View', fg='White', bg='blue', command=Sateliteview)
    nrmlview = tk.Button(button_window, text='Normal View', fg='white', bg='black', command=Nrmlview)
    osm_button = tk.Button(button_window, text='OpenStreetMap View', fg='black', bg='green', command=OpenStreetMapView)

    butonsRed = {"button_1": button_1, "entry": entry, "button_2" : button_2, "save_button": save_button, "satnav": satnav, "nrmlview": nrmlview, "osm_button":osm_button}

    for index, btn in enumerate(list(butonsRed.values())):
        btn.grid(row=0, column = index)


    # Pack the buttons side by side
    # button_1.pack(side="top", padx=10, pady=20)
    # entry.pack(side="top", padx=10, pady=10)
    # button_2.pack(side="top", padx=10, pady=10)
    # save_button.pack(side="top", padx=10, pady=10)
    # satnav.pack(side="top", padx=10, pady=10)
    # nrmlview.pack(side="top", padx=10, pady=10)
    # osm_button.pack(side="top", padx=10, pady=10)

    # Flight Data Entry Section
    label_time_in = tk.Label(button_window, text="Time In:", font=("Arial", 12))
    entry_time_in = tk.Entry(button_window, font=("Arial", 12))

    label_speed = tk.Label(button_window, text="Speed:", font=("Arial", 12))
    entry_speed = tk.Entry(button_window, font=("Arial", 12))

    add_flight_button = tk.Button(button_window, text="Add Flight", command=add_flight)

    label_flight_code = tk.Label(button_window, text="Flight Code:", font=("Arial", 12))
    entry_flight_code = tk.Entry(button_window, font=("Arial", 12))

    label_aircraft_reg = tk.Label(button_window, text="Aircraft Registration:", font=("Arial", 12))
    entry_aircraft_reg = tk.Entry(button_window, font=("Arial", 12))

    label_aircraft_name = tk.Label(button_window, text="Aircraft Name:", font=("Arial", 12))
    entry_aircraft_name = tk.Entry(button_window, font=("Arial", 12))

    label_arrival = tk.Label(button_window, text="Arrival:", font=("Arial", 12))
    entry_arrival = tk.Entry(button_window, font=("Arial", 12))

    label_destination = tk.Label(button_window, text="Destination:", font=("Arial", 12))
    entry_destination = tk.Entry(button_window, font=("Arial", 12))

    label_priority = tk.Label(button_window, text="Priority:", font=("Arial", 12))
    entry_priority = tk.Entry(button_window, font=("Arial", 12))

    add_flight_button = tk.Button(button_window, text="Add Flight", command=add_flight)

    # Pack the flight data entry widgets
    label_flight_code.grid(row=1, column=0)
    entry_flight_code.grid(row=2, column=0)
    label_aircraft_reg.grid(row=3, column=0)
    entry_aircraft_reg.grid(row=4, column=0)
    label_aircraft_name.grid(row=5, column=0)
    entry_aircraft_name.grid(row=6, column=0)
    label_arrival.grid(row=7, column=0)
    entry_arrival.grid(row=8, column=0)
    label_destination.grid(row=9, column=0)
    entry_destination.grid(row=10, column=0)
    label_priority.grid(row=11, column=0)
    entry_priority.grid(row=12, column=0)
    label_time_in.grid(row=13, column=0)
    entry_time_in.grid(row=14, column=0)
    label_speed.grid(row=15, column=0)
    entry_speed.grid(row=16, column=0)
    add_flight_button.grid(row=17, column=0)

    global frame
    frame = tk.Frame(master=button_window)
    frame.grid(row=1, column=1, rowspan=10, columnspan=3)


    # Flight List
    global flight_list, flight_list_label
    flight_list_label = tk.Label(frame, text="Flight List:", font=("Arial", 14, "bold"))
    flight_list_label.grid(row=1, column=1, rowspan=10, columnspan=3)

    flight_list_columns = ("Flight Code", "Aircraft Reg", "Aircraft Name", "Arrival", "Destination", "Priority", "Time In", "Speed", "Timestamp")
    flight_list = ttk.Treeview(frame, columns=flight_list_columns, show="headings")

    global flight_list1, flight_list_label1
    flight_list_label1 = tk.Label(frame, text="Flight List:", font=("Arial", 14, "bold"))
    flight_list_label1.grid(row=10, column=1, rowspan=10, columnspan=10, padx= 10, pady=10)

    flight_list_columns1 = ("Flight Code", "Aircraft Reg", "Aircraft Name", "rwy", "gate no", "Priority", "Taxiwayn", "Speed", "Timestamp")
    flight_list1 = ttk.Treeview(frame, columns=flight_list_columns, show="headings")
    flight_list1.grid(row=5, column=1, rowspan= 10, columnspan= 10, padx=10, pady=10)



    for column in flight_list_columns:
        flight_list.heading(column, text=column)
        flight_list.column(column, width=100, anchor="center")

    flight_list.grid(row=3, column=1, rowspan= 10, columnspan= 10)

    # Load initial flight data
    global flights
    flights = load_flight_data()
    update_flight_list()


# Create a button to open the button window
open_button_window_button = tk.Button(root_tk, text="Open Button Window", command=open_button_window)
open_button_window_button.pack()


# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=1000, height=700, corner_radius=0)
map_widget.pack(fill="both", expand=True)

# set other tile server (standard is OpenStreetMap)

def Nrmlview():
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

def Sateliteview():
     map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

def save_map_view():
    # Get the coordinates and dimensions of the map widget
    x = root_tk.winfo_x() + map_widget.winfo_x()
    y = root_tk.winfo_y() + map_widget.winfo_y()
    width = map_widget.winfo_width()
    height = map_widget.winfo_height()
    
    # Capture the map view as an image
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    
    # Ask the user to choose a file location for saving the image
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    
    if file_path:
        # Save the image to the chosen file location
        screenshot.save(file_path)


# set current position and zoom
map_widget.set_position(51.4198666 , -0.2891967, marker=True)  # Berlin, Germany
# map_widget.set_zoom(17)

# set current position with address
# map_widget.set_address("Berlin Germany", marker=False)

def marker_click(marker):
    print(f"marker clicked - text: {marker.text}  position: {marker.position}")

# set a position marker (also with a custom color and command on click)
# marker_3.set_position(...)
# marker_3.set_text(...)
# marker_3.delete()

# set a path
# path_1.remove_position(...)
# path_1.delete()

def BringDaLimo():
    addr = entry.get()
    map_widget.set_address(addr, marker=True, text=addr)

def TheMagicSchoolBus():
    x = random.uniform(-200, 200)
    y = random.uniform(-200, 200)
    map_widget.set_position(x , y, marker=True)  # Berlin, Germany


def load_flight_data():
    try:
        with open("flights.json", "r") as file:
            loaded_data = json.load(file)
            return loaded_data
    except FileNotFoundError:
        return {}

def save_flight_data():
    with open("flights.json", "w") as file:
        json.dump(flights, file)

def generate_timestamp():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def add_flight():
    flight_code = entry_flight_code.get()
    aircraft_reg = entry_aircraft_reg.get()
    aircraft_name = entry_aircraft_name.get()
    arrival = entry_arrival.get()
    destination = entry_destination.get()
    priority = entry_priority.get()

    timestamp = generate_timestamp()

    flights[flight_code] = {
        'aircraft_reg': aircraft_reg,
        'aircraft_name': aircraft_name,
        'arrival': arrival,
        'destination': destination,
        'priority': priority,
        'timestamp': timestamp
    }

    save_flight_data()  # Save flight data after adding
    update_flight_list()  # Update the flight list after adding

# Function to update the flight list panel
def update_flight_list():
    # Clear the current list
    for item in flight_list.get_children():
        flight_list.delete(item)

    for flight_code, data in flights.items():
        flight_list.insert('', 'end', values=(flight_code, data['aircraft_reg'], data['aircraft_name'], data['arrival'], data['destination'], data['priority'], data['timestamp']))

# Create a function to open the button window
def open_button_window():
    global entry_flight_code, entry_aircraft_reg, entry_aircraft_name, entry_arrival, entry_destination, entry_priority
    # Create a new tkinter window for the buttons
    button_window = tk.Toplevel(root_tk)
    button_window.title("Button Window")

def OpenStreetMapView():
    map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png", max_zoom=19)


# Function to add a flight
def add_flight():
    flight_code = entry_flight_code.get()
    aircraft_reg = entry_aircraft_reg.get()
    aircraft_name = entry_aircraft_name.get()
    arrival = entry_arrival.get()
    destination = entry_destination.get()
    priority = entry_priority.get()
    time_in = entry_time_in.get()  # Added 'time in' field
    speed = entry_speed.get()  # Added 'speed' field

    timestamp = generate_timestamp()

    flights[flight_code] = {
        'aircraft_reg': aircraft_reg,
        'aircraft_name': aircraft_name,
        'arrival': arrival,
        'destination': destination,
        'priority': priority,
        'time_in': time_in,  # Store 'time in'
        'speed': speed,  # Store 'speed'
        'timestamp': timestamp
    }

    save_flight_data()  # Save flight data after adding
    update_flight_list()  # Update the flight list after adding

# Function to update the flight list panel
def update_flight_list():
    # Clear the current list
    for item in flight_list.get_children():
        flight_list.delete(item)

    for flight_code, data in flights.items():
        flight_list.insert('', 'end', values=(flight_code, data['aircraft_reg'], data['aircraft_name'], data['arrival'], data['destination'], data['priority'], data['time_in'], data['speed'], data['timestamp']))


# Create a function to open the button window
def open_button_window():
    global entry_flight_code, entry_aircraft_reg, entry_aircraft_name, entry_arrival, entry_destination, entry_priority, entry_time_in, entry_speed
    # Create a new tkinter window for the buttons
    button_window = tk.Toplevel(root_tk)
    button_window.title("Button Window")

    label_time_in = tk.Label(button_window, text="Time In:", font=("Arial", 12))
    entry_time_in = tk.Entry(button_window, font=("Arial", 12))

    label_speed = tk.Label(button_window, text="Speed:", font=("Arial", 12))
    entry_speed = tk.Entry(button_window, font=("Arial", 12))

    add_flight_button = tk.Button(button_window, text="Add Flight", command=add_flight)

    label_flight_code = tk.Label(button_window, text="Flight Code:", font=("Arial", 12))
    entry_flight_code = tk.Entry(button_window, font=("Arial", 12))

    label_aircraft_reg = tk.Label(button_window, text="Aircraft Registration:", font=("Arial", 12))
    entry_aircraft_reg = tk.Entry(button_window, font=("Arial", 12))

    label_aircraft_name = tk.Label(button_window, text="Aircraft Name:", font=("Arial", 12))
    entry_aircraft_name = tk.Entry(button_window, font=("Arial", 12))

    label_arrival = tk.Label(button_window, text="Arrival:", font=("Arial", 12))
    entry_arrival = tk.Entry(button_window, font=("Arial", 12))

    label_destination = tk.Label(button_window, text="Destination:", font=("Arial", 12))
    entry_destination = tk.Entry(button_window, font=("Arial", 12))

    label_priority = tk.Label(button_window, text="Priority:", font=("Arial", 12))
    entry_priority = tk.Entry(button_window, font=("Arial", 12))

    add_flight_button = tk.Button(button_window, text="Add Flight", command=add_flight)

    label_flight_code.grid(row=1, column=0)
    entry_flight_code.grid(row=1, column=0)

    label_aircraft_reg.grid(row=1, column=0)
    entry_aircraft_reg.grid(row=1, column=0)

    label_aircraft_name.grid(row=1, column=0)
    entry_aircraft_name.grid(row=1, column=0)

    label_arrival.grid(row=1, column=0)
    entry_arrival.grid(row=1, column=0)

    label_destination.grid(row=1, column=0)
    entry_destination.grid(row=1, column=0)

    label_priority.grid(row=1, column=0)
    entry_priority.grid(row=1, column=0)

    add_flight_button.grid(row=1, column=0)

    # Flight List
    flight_list_label = tk.Label(button_window, text="Flight List:", font=("Arial", 14, "bold"))
    flight_list_label.grid(row=1, column=0)

    flight_list_columns = ("Flight Code", "Aircraft Reg", "Aircraft Name", "Arrival", "Destination", "Priority", "Timestamp")
    global flight_list
    flight_list = ttk.Treeview(button_window, columns=flight_list_columns, show="headings")

    label_time_in.grid(row=1, column=0)
    entry_time_in.grid(row=1, column=0)

    label_speed.grid(row=1, column=0)
    entry_speed.grid(row=1, column=0)

    add_flight_button.grid(row=1, column=0)

    for column in flight_list_columns:
        flight_list.heading(column, text=column)
        flight_list.column(column, width=100, anchor="center")  # Adjust column width and alignment as needed

    flight_list.grid(row=1, column=0)

    # Load initial flight data
    global flights
    flights = load_flight_data()
    update_flight_list()

root_tk.mainloop()

