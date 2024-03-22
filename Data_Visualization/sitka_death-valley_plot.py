### Author: KaruppuSwamy Thangaraj ###
### Date: 12-Mar-2024              ###

from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt

# Sitka data collection
path_sitka = Path('sitka_weather_2021_simple.csv')
lines_sitka = path_sitka.read_text().splitlines()
reader_sitka = csv.reader(lines_sitka)
header_row_sitka = next(reader_sitka)

# Death Valley data collection
path_dv = Path('death_valley_2021_simple.csv')
lines_dv = path_dv.read_text().splitlines()
reader_dv = csv.reader(lines_dv)
header_row_dv = next(reader_dv)

# Here columns are in different index for two cities
print(header_row_sitka)
print(header_row_dv)

# Find right index for Date and Max temperature
temp_max_index_sitka = header_row_sitka.index('TMAX')
temp_max_index_dv = header_row_dv.index('TMAX')
print(f"TMAX: Sitka Index: {temp_max_index_sitka} DV Index: {temp_max_index_dv}")
date_index_sitka = header_row_sitka.index('DATE')
date_index_dv = header_row_dv.index('DATE')
print(f"DATE: Sitka Index: {date_index_sitka} DV Index: {date_index_dv}")

# Initialize date and high temperature lists
dates_sitka, dates_dv, highs_sitka, highs_dv = [], [], [], []

# get date and high temperature list prepared for Sitka
for row in reader_sitka:
    try:
        date = datetime.strptime(row[date_index_sitka], '%Y-%m-%d')
        high = int(row[temp_max_index_sitka])
    except ValueError:
        print("Missing date / Max Temp value in a row of Sitka")
    else:
        dates_sitka.append(date)
        highs_sitka.append(high)

# get date and high temperature list prepared for Death Valley
for row in reader_dv:
    try:
        date = datetime.strptime(row[date_index_dv], '%Y-%m-%d')
        high = int(row[temp_max_index_dv])
    # No. of rows are different for two cities (some date may be missing)
    except ValueError:
        print("Missing date / Max Temp value in a row of Death Valley")
    else:
        dates_dv.append(date)
        highs_dv.append(high)

# Preparing plot
plt.style.use('seaborn')     
fig, ax = plt.subplots()
ax.plot(dates_sitka, highs_sitka, color='green')
ax.plot(dates_dv, highs_dv, color='red')

# Format plot
ax.set_title("Daily High Temperature in Sitka and Death Valley, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()     # Draws date label diagonally
ax.set_ylabel('Temperature (F)', fontsize=16)
plt.legend(['Sitka', 'Death Valley'])

# Save the Plot as image file
plt.savefig('sitka_death-valley_temperature.png', bbox_inches='tight')

# Show the Plot
plt.show()


