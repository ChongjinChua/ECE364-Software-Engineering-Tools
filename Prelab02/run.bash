#!/bin/bash

#$Author: ee364g13 $
#$Date: 2016-01-24 16:42:21 -0500 (Sun, 24 Jan 2016) $
#$Revisions$
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364g13/Prelab02/run.bash $
#$Id: run.bash 86595 2016-01-24 21:42:21Z ee364g13 $

param_num=$#
param_val=($@)
USAGE="Usage: run.bash <source file> <output file>"
ERROR="error: ${param_val[0]} could not be compiled!"

#ONLY ALLOWS 1 ARGUMENT
if (($param_num != 2)); then
    echo "$USAGE"
    exit 1
fi

touch_file=${param_val[1]}

[[ -e quick_sim ]] && rm quick_sim

gcc ${param_val[0]} -o quick_sim;
if (( $? != 0 )); then
    echo "$ERROR"
    exit 1
elif [[ -e ${param_val[1]} ]]; then
    read -p "${param_val[1]} exists. Would you like to delete it? " del_input
    case "$del_input" in
	"n" | "no" | "No" | "NO") 
	    read -p "Enter a new filename: " newname_input
	    rm $newname_input 2>/dev/null
	    touch_file=$newname_input
	    ;;
	"y" | "yes" | "Yes" | "YES")
	    rm ${param_val[1]}
	    ;;
	*)
	    echo "invalid input";
	    exit 1
	    ;;
    esac
fi

touch $touch_file

A_cache=(1 2 4 8 16 32); A_iwidth=(1 2 4 8 16)

let shortest_time=99999999
let shortest_name=error
let shortest_cache=error
let shortest_iwidth=error

for I in ${A_cache[*]}; do
    for J in ${A_iwidth[*]}; do
	data_output=$(./quick_sim $I $J a)
	cpi_a=$(echo $data_output | cut -d':' -f8)
	time_a=$(echo $data_output | cut -d':' -f10)
	echo "AMD Opteron:$I:$J:$cpi_a:$time_a" >> $touch_file
	
	data_output=$(./quick_sim $I $J i)
	cpi_i=$(echo $data_output | cut -d':' -f8)
	time_i=$(echo $data_output | cut -d':' -f10)
	echo "Intel Core i7:$I:$J:$cpi_i:$time_i" >> $touch_file

	if (( $time_a < $shortest_time )); then
	    shortest_time=$time_a
	    shortest_name="AMD Opteron"
	    shortest_iwidth=$J
	    shortest_cache=$I
	fi
	if (( $time_i < $shortest_time )); then
	    shortest_time=$time_i
	    shortest_name="Intel Core i7"	    
	    shortest_iwidth=$J
	    shortest_cache=$I	    
	fi
    done
done

echo "Fastest run time achieved by $shortest_name with cache size $shortest_cache and issue width $shortest_iwidth was $shortest_time"

exit 0