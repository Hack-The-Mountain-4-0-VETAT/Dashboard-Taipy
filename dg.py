import random

# Define a dictionary to store the year-wise and month-wise electricity usage
electricity_usage = {}

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# For each year and each month, generate a random number between 1000 and 5000 to simulate the electricity usage for that month
for year in range(1, 6):
    electricity_usage[year] = {}
    for month in months:
        electricity_usage[year][month] = random.randint(1000, 5000)

import csv
# Open a new CSV file in write mode
with open('electricity_usage.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['YearMonth', 'Usage'])

    # Iterate over the years from 2001 to 2010, and for each month, write a row to the CSV file
    for year in range(2001, 2011):
        for month in range(1, 13):
            usage = random.randint(1000, 5000)
            writer.writerow([f'{year}/{month}', usage])