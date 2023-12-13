import matplotlib.pyplot as plt
import csv 


# file_path_2 = '/home/pi/C-0049-bench30min.csv'
# file_path_2 = '/home/pi/kz-0028-bench30min.csv'
file_path_2 = '/home/pi/kz-0028-bench30min.csv'

def read_csv(file_path):
   with open(file_path, "r") as f:
       reader = csv.reader(f)
       data = list(reader)
   # print(data)
   return data


# file1_data = read_csv(file_path_1)
file2_data = read_csv(file_path_2)
#file3_data = read_csv(file_path_3)
#file4_data = read_csv(file_path_4)
#file5_data = read_csv(file_path_5)

#file1_x = [float(file1_data[i][0]) for i in range(len(file1_data))][::-1]
#file1_y = [float(file1_data[i][1]) for i in range(len(file1_data))]

# file2_x = [float(file2_data[i][0]) for i in range(len(file2_data))][::-1]
file2_x = [float(file2_data[i][0]) for i in range(len(file2_data))]
file2_y = [float(file2_data[i][1]) for i in range(len(file2_data))]

#file3_x = [float(file3_data[i][0]) for i in range(len(file3_data))][::-1]
#file3_y = [float(file3_data[i][1]) for i in range(len(file3_data))]

#file4_x = [float(file4_data[i][0]) for i in range(len(file4_data))][::-1]
#file4_y = [float(file4_data[i][1]) for i in range(len(file4_data))]

#file5_x = [float(file5_data[i][0]) for i in range(len(file5_data))][::-1]
#file5_y = [float(file5_data[i][1]) for i in range(len(file5_data))]

plt.grid(True)

#plt.plot(file1_x, file1_y, color='red', label='{}'.format(file_path_1.rstrip('.csv')))
plt.plot(file2_x, file2_y, color='blue', label='{}'.format(file_path_2.rstrip('.csv')))
plt.scatter(file2_x, file2_y)
for i, text in enumerate(file2_y):
    plt.annotate(f"{text}", (file2_x[i],file2_y[i]), textcoords="offset points", xytext=(0,20), ha="center")
#plt.plot(file3_x, file3_y, color='green', label='{}'.format(file_path_3.rstrip('.csv')))
#plt.plot(file4_x, file4_y, color='yellow', label='{}'.format(file_path_4.rstrip('.csv')))
#plt.plot(file5_x, file5_y, color='cyan', label='{}'.format(file_path_5.rstrip('.csv')))

plt.title("CPU Temperature Bench Test in 20 minutes")
new_yticks = [30,40,50,60,70]
plt.yticks(new_yticks)
new_xticks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
plt.xticks(new_xticks)
plt.xlabel('Times(minutes)')
plt.ylabel('Temperature of CPU')

plt.legend()

plt.show()

