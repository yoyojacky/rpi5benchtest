#!/bin/bash
while true
do
	vcgencmd measure_temp | tr '\n' '\t' ; vcgencmd measure_clock arm
	sleep 0.2
done 
