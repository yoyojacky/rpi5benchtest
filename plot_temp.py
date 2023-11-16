import matplotlib.pyplot as plt
import csv 


x = []
x1 = [] 

# file_path_1 = 'armor-bench20min.csv'
file_path_1 = 'metal-bench20min.csv'
file_path_2 = 'pibench20min.csv'


def read_csv(file_path):
   with open(file_path, "r") as f:
       reader = csv.reader(f)
       data = list(reader)
   # print(data)
   return data


file1_data = read_csv(file_path_1)
file2_data = read_csv(file_path_2)

file1_x = [float(file1_data[i][0]) for i in range(len(file1_data))][::-1]
file1_y = [float(file1_data[i][1]) for i in range(len(file1_data))]

file2_x = [float(file2_data[i][0]) for i in range(len(file2_data))][::-1]
file2_y = [float(file2_data[i][1]) for i in range(len(file2_data))]


plt.plot(file1_x, file1_y, color='blue', label='{}'.format(file_path_1.rstrip('.csv')))
plt.grid(True)
plt.plot(file2_x, file2_y, color='red', label='{}'.format(file_path_2.rstrip('.csv')))

plt.title("CPU Temperature Bench Test in 20 minutes")
plt.xlabel('Times(1200 seconds)')
plt.ylabel('Temperature of CPU')

plt.legend()

plt.show()

