#!/bin/bash

#$Author: ee364g13 $
#$Date: 2016-01-23 01:43:14 -0500 (Sat, 23 Jan 2016) $
#$Revisions$
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364g13/Prelab02/process_temps.bash $
#$Id: process_temps.bash 86528 2016-01-23 06:43:14Z ee364g13 $

param_num=$#
param_val=$@
USAGE="Usage: process_temps.bash <input file>"
ERROR="Error: $param_val is not a readable file"

#ONLY ALLOWS 1 ARGUMENT
if (($param_num != 1)); then
    echo "$USAGE"
    exit 1
elif [[ ! -e $param_val || ! -r $param_val ]]; then
    echo "$ERROR"
    exit 2
fi

while read line;do
    time_var=$(echo $line | cut -d' ' -f1)
    temp_var=$(echo $line | cut -d' ' -f2-)

    if [[ "$time_var" == "time" ]]; then
	continue
    fi

    let sum=0
    A=($temp_var)
    for I in ${A[*]}; do
	(( sum=$sum+$I ))
    done
    (( avg=$sum/${#A[*]} ))

    echo "Average temperature for time $time_var was $avg C."

done <$param_val

exit 0