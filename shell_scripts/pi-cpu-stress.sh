#!/bin/bash
# Raspberry Pi stress CPU temperature measurement script.
#
# varaibles
test_run=1
test_results_file="/home/pi/cpu_temp_$test_run.log"
stress_length="20m"

# Verify stress-ng is installed.
if ! [ -x "$(command -v stress-ng)" ]; then
	printf "Error: stress-ng not installed.\n"
	printf "To install: sudo apt install -y stress-ng\n" >&2
	exit 1
fi 

printf "Logging temperature and throtting data to: $test_results_file\n"

# Start logging temperature data in the background.
while true;
do 
	date | tr '\n' '\t' >> $test_results_file;

	vcgencmd measure_temp | tr -d "temp=" | tr -d "'C" | tr '\n' '\t' >> $test_results_file;
	vcgencmd get_throttled | tr -d "throttled=" | tr '\n' '\t' >> $test_results_file;

	vcgencmd measure_clock arm | sed 's/^.*=//' >> $test_results_file;
	sleep 5;
done & 

PROC_ID=$!

trap "kill $PROC_ID" EXIT

printf "Waiting 20 minutes for stable idle temperature...\n"
sleep  300
printf "Beginning $stress_length stress test...\n"
stress-ng -c 4 --timeout $stress_length
printf "Waiting 5 minutes to return to idle temperatue...\n"
sleep  300
printf "Test complete.\n"

