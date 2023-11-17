import matplotlib.pyplot as plt
import csv 


x = []
x1 = [] 

# file_path_1 = 'armor-bench20min.csv'
# file_path_1 = 'metal-bench20min.csv'
# file_path_3 = 'metal-fan-bench20min.csv'
file_path_1 = 'rpi5-case-normal-use.csv'
file_path_3 = 'rpi5-case-bench20min.csv'
file_path_2 = 'pibench20min.csv'


def read_csv(file_path):
   with open(file_path, "r") as f:
       reader = csv.reader(f)
       data = list(reader)
   # print(data)
   return data


file1_data = read_csv(file_path_1)
file2_data = read_csv(file_path_2)
file3_data = read_csv(file_path_3)

file1_x = [float(file1_data[i][0]) for i in range(len(file1_data))][::-1]
file1_y = [float(file1_data[i][1]) for i in range(len(file1_data))]

file2_x = [float(file2_data[i][0]) for i in range(len(file2_data))][::-1]
file2_y = [float(file2_data[i][1]) for i in range(len(file2_data))]

file3_x = [float(file3_data[i][0]) for i in range(len(file3_data))][::-1]
file3_y = [float(file3_data[i][1]) for i in range(len(file3_data))]


plt.grid(True)
plt.plot(file1_x, file1_y, color='blue', label='{}'.format(file_path_1.rstrip('.csv')))
plt.plot(file2_x, file2_y, color='red', label='{}'.format(file_path_2.rstrip('.csv')))
plt.plot(file3_x, file3_y, color='green', label='{}'.format(file_path_3.rstrip('.csv')))

plt.title("CPU Temperature Bench Test in 20 minutes")
plt.xlabel('Times(1200 seconds)')
plt.ylabel('Temperature of CPU')

plt.legend()

plt.show()

