from gpiozero import CPUTemperature
import time
import matplotlib.pyplot as plt


cpu = CPUTemperature()

plt.ion()
x = []
y = []
count = 0

filename = '/home/pi/kz-0027-bench30min.csv'

def write_temp(temp):
    with open(filename, 'a') as log:
        # log.write("{0},{1},".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))
        log.write("{0},{1}".format(count, str(temp)))
        log.write("\n")

        
def graph(temp):
    y.append(temp)
    x.append(time.time())
    plt.clf()
    plt.scatter(x,y)
    plt.grid(True)
    plt.plot(x,y, marker='o', color='blue')
    for i, temp in enumerate(y):
        plt.annotate(f'{temp}',(x[i], y[i]), textcoords="offset points", xytext=(0, 20), ha="center")
    plt.title('sysbench pressed temperature of CPU test')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.draw()


while True:
    temp = cpu.temperature
    write_temp(temp)
    graph(temp)
    plt.pause(60)
    count += 1
    print(count)
    
    if count == 31:
        break

