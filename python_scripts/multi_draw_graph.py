import os
import matplotlib.pyplot as plt
import csv 
from random import randint


cwd = os.getcwd()
print(cwd)

files = os.listdir(cwd)

csv_files = [file for file in files if file.endswith('.csv')]
print(csv_files)


for csv_file in csv_files:
    file_path = os.path.join(cwd, csv_file)

    with open(file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        data = list(csv_reader)
        x_data = [row[0] for row in data]
        y_data = [float(row[1]) for row in data]
        color = ['red','blue','green','black','pink']
        color = color[randint(0, len(color))]

        plt.plot(x_data, y_data, label=csv_file, color="{}".format(color))

plt.legend()

plt.title("CPU temperature on bench 20 minutes")
plt.xlabel('Times (1200 seconds)')
plt.ylabel('Temperature of CPU')


plt.show()
