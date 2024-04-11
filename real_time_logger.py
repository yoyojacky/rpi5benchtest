from gpiozero import CPUTemperature
import time
import matplotlib.pyplot as plt


cpu = CPUTemperature()

plt.ion()
x = []
y = []
count = 0

# filename = '/home/pi/dualpipe-icetower-overclock-bench30min.csv'
# filename = '/home/pi/yuanqihe-bench30min.csv'
# filename = '/home/pi/new-watercooler-bench30min.csv'
# filename = '/home/pi/c-0053-bench30min.csv'
# filename = '/home/pi/EP-0222-PMIC-BTN-for-pi5-bench30min.csv'
# filename = '/home/pi/ZP-0185-normaluse-bench30min.csv'
# filename = '/home/pi/ZP-0181-game5pi-bench30min.csv'
# filename = '/home/pi/icepump-bench30min.csv'
# filename = '/home/pi/EP-0222-bench30min.csv'
# filename = '/home/pi/C-0052-dualfan-bench30min.csv'
# filename = '/home/pi/EP-0226-acrylic-btn-bench30min.csv'
filename = '/home/pi/c-0052-2-bench30min.csv'

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
        plt.annotate(f'{int(round(temp))}',(x[i], y[i]), textcoords="offset points", xytext=(0, 20), ha="center")
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

