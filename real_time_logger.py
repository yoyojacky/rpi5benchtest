from gpiozero import CPUTemperature
from time import sleep, strftime, time
import matplotlib.pyplot as plt


cpu = CPUTemperature()

plt.ion()
x = []
y = []
count = 1200

def write_temp(temp):
    with open('/home/pi/armor-bench20min.csv', 'a') as log:
        # log.write("{0},{1},".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))
        log.write("{0},{1}".format(count, str(temp)))
        log.write("\n")


def graph(temp):
    y.append(temp)
    x.append(time())
    plt.clf()
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.draw()


while True:
    temp = cpu.temperature
    write_temp(temp)
    graph(temp)
    plt.pause(1)
    count -= 1
    print(count)
    if count == 0:
        break

