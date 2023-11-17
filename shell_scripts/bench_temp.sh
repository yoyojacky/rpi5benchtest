#!/bin/bash
while true
do 
	sysbench --test=cpu --cpu-max-prime=20000 --threads=4 run 
	sleep 0.1
done 
