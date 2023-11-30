import matplotlib.pyplot as plt
import csv 


# file_path_1 = 'official-heatsink-bench20min.csv'
# file_path_1 = 'metal-fan-bench20min.csv'
# file_path_3 = 'metal-fan-bench20min.csv'
# file_path_1 = 'armor-case-thermal-normal-use.csv'
# file_path_1 = 'armor-case-thermal-bench20min.csv'
# file_path_1 = 'metal-3510-bench20min.csv'
# file_path_1 = 'pibench20min.csv'
file_path_1 = 'no-heatsink-no-fan.csv'
#file_path_2 = 'official-heatsink-bench20min.csv'
# file_path_2 = 'armor-case-normal-use.csv'
# file_path_4 = 'armor-case-bench20min.csv'
#file_path_4 = 'heatsink-case-normal-use.csv'
#file_path_3 = 'armor-case-3mm-bench20min.csv'
file_path_2 = 'icetower-btn-case-thermal-bench20min.csv'
file_path_3 = 'official-heatsink-bench20min.csv'
file_path_4 = 'icetower-btn-case-thermal-overclock20min.csv'
#file_path_4 = 'open-armor-case-3mm-normal-use.csv'
#file_path_5 = 'official-heatsink-normal-use.csv'
#file_path_3 = 'armor-case-selfdev-bench20min.csv'
#file_path_4 = 'armor-case-selfdev-normal-use.csv'


def read_csv(file_path):
   with open(file_path, "r") as f:
       reader = csv.reader(f)
       data = list(reader)
   # print(data)
   return data


file1_data = read_csv(file_path_1)
file2_data = read_csv(file_path_2)
file3_data = read_csv(file_path_3)
file4_data = read_csv(file_path_4)
#file5_data = read_csv(file_path_5)

file1_x = [float(file1_data[i][0]) for i in range(len(file1_data))][::-1]
file1_y = [float(file1_data[i][1]) for i in range(len(file1_data))]

file2_x = [float(file2_data[i][0]) for i in range(len(file2_data))][::-1]
file2_y = [float(file2_data[i][1]) for i in range(len(file2_data))]

file3_x = [float(file3_data[i][0]) for i in range(len(file3_data))][::-1]
file3_y = [float(file3_data[i][1]) for i in range(len(file3_data))]

file4_x = [float(file4_data[i][0]) for i in range(len(file4_data))][::-1]
file4_y = [float(file4_data[i][1]) for i in range(len(file4_data))]

#file5_x = [float(file5_data[i][0]) for i in range(len(file5_data))][::-1]
#file5_y = [float(file5_data[i][1]) for i in range(len(file5_data))]

plt.grid(True)

plt.plot(file1_x, file1_y, color='red', label='{}'.format(file_path_1.rstrip('.csv')))
plt.plot(file2_x, file2_y, color='blue', label='{}'.format(file_path_2.rstrip('.csv')))
plt.plot(file3_x, file3_y, color='green', label='{}'.format(file_path_3.rstrip('.csv')))
plt.plot(file4_x, file4_y, color='yellow', label='{}'.format(file_path_4.rstrip('.csv')))
#plt.plot(file5_x, file5_y, color='cyan', label='{}'.format(file_path_5.rstrip('.csv')))

plt.title("CPU Temperature Bench Test in 20 minutes")
plt.xlabel('Times(1200 seconds)')
plt.ylabel('Temperature of CPU')

plt.legend()

plt.show()

