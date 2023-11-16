# rpi5benchtest
bench test result drawing 
## How to use
1. Install sysbench package
```bash
sudo apt update
sudo apt upgrade -y
sudo apt -y install sysbench vim
sudo apt -y install stress-ng
sudo apt -y install python3-matplotlib
```
2. Download the repository
```bash
git clone https://github.com/yoyojacky/rpi5benchtest.git
cd rpi5benchtest/
```
3. Press the CPU by using sysbench command in a shell loop
```bash
while true
do
   sysbench --test=cpu --max-cpu-prime=20000 --threads=4 run
   sleep 0.1
done
```
4. Execute the python script to record the temperature of CPU and save it to a .csv file, and draw the graph at the same time.
```bash
python3 real_time_logger.py
```
It will take 1200 seconds to record the temperature. after that, it will terminate the process.
5. plot graph between two csv file, for example, there is an record file called `pibench20min.csv` which is bench test on raspberry pi without any heat sinks and fan, and another file called `armor-bench20min.csv` which means that the record is baseed on armor case and fan. 
```bash
python3 plot_temp.py
```
It will draw two graphs in legend mode.
