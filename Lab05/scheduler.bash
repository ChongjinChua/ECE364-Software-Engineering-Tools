#! /bin/bash

param_num=$#
param_val=$@
param_val_out=$(echo $param_val | cut -d'/' -f2 | cut -d'.' -f1
USAGE="Usage: scheduler.bash <filename>" #return code 1
ERROR_NEXIST="Error reading input file: $param_val"  #return code 2


if (($param_num != 1)); then
    echo "$USAGE"
    exit 1
elif [[ ! -e $param_val && ! -r $param_val ]]; then
    echo "$ERROR_NEXIST"
    exit 2


fi
