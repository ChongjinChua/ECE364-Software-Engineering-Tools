#!/bin/bash

#$Author: ee364g13 $
#$Date: 2016-01-17 12:47:24 -0500 (Sun, 17 Jan 2016) $
#$Revisions$
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364g13/Prelab01/sensor_sum.sh $
#$Id: sensor_sum.sh 85308 2016-01-17 17:47:24Z ee364g13 $

param_num=$#
param_val=$@
USAGE="usage: sensor_sum.sh"
ERROR="error: $param_val is not a readable file!"

#ONLY ALLOWS 1 ARGUMENT, also make sure file is readable
if (($param_num != 1)); then
    echo "$USAGE"
    exit 1
elif [[ ! -r $param_val ]]; then
    echo "$ERROR"
    exit 1
fi

let total_sum=0
while read -u 3 -r line; do

    for (( I=2; I < 5; I++ )); do
	sum=$(echo $line | cut -d' ' -f$I- | cut -d' ' -f1)
	(( total_sum=total_sum+sum ))
    done

    echo "$(echo $line | cut -d'-' -f1) $total_sum"
    
    sum=0; total_sum=0
done 3<$param_val

exit 0



