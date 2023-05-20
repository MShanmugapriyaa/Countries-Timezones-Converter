import tkinter as tk
from datetime import datetime
import pytz

# Fetch all time zones and their country names
all_timezones = pytz.all_timezones
timezones = {}
for timezone in all_timezones:
    try:
        country = timezone.split('/')[0]
        timezones[country] = timezone
    except IndexError:
        continue

def convert_time():
    country1 = country1_var.get()
    country2 = country2_var.get()
    time_str = time_entry.get()

    current_date = datetime.now().date()
    time = datetime.strptime(time_str, '%I:%M %p').time()
    time = datetime.combine(current_date, time)

    timezone1 = pytz.timezone(timezones[country1])
    timezone2 = pytz.timezone(timezones[country2])
    time_in_timezone1 = timezone1.localize(time)
    time_in_timezone2 = time_in_timezone1.astimezone(timezone2)

    converted_time_str = time_in_timezone2.strftime('%I:%M %p')

    result_label.config(text="Time in {0}: {1}\nTime in {2}: {3}".format(country1, time.strftime('%I:%M %p'),
                                                                         country2, converted_time_str))

window = tk.Tk()
window.title("Time Converter")

country1_label = tk.Label(window, text="Country 1:")
country2_label = tk.Label(window, text="Country 2:")
time_label = tk.Label(window, text="Time (HH:MM AM/PM):")
result_label = tk.Label(window, text="")

country1_var = tk.StringVar(window)
country1_entry = tk.OptionMenu(window, country1_var, *timezones.keys())
country1_entry.config(width=20)
country2_var = tk.StringVar(window)
country2_entry = tk.OptionMenu(window, country2_var, *timezones.keys())
country2_entry.config(width=20)
time_entry = tk.Entry(window)

convert_button = tk.Button(window, text="Convert", command=convert_time)

country1_label.grid(row=0, column=0, padx=10, pady=10)
country1_entry.grid(row=0, column=1, padx=10, pady=10)
country2_label.grid(row=1, column=0, padx=10, pady=10)
country2_entry.grid(row=1, column=1, padx=10, pady=10)
time_label.grid(row=2, column=0, padx=10, pady=10)
time_entry.grid(row=2, column=1, padx=10, pady=10)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
