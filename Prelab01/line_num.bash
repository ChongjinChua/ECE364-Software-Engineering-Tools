#!/bin/bash

#$Author: ee364g13 $
#$Date: 2016-01-17 11:36:15 -0500 (Sun, 17 Jan 2016) $
#$Revisions$
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364g13/Prelab01/line_num.bash $
#$Id: line_num.bash 85297 2016-01-17 16:36:15Z ee364g13 $

param_num=$#
param_val=$@
USAGE="Usage: line_num.bash <filename>"
ERROR="Cannot read "$param_val""
counter="1"

if [[ "$param_num" != "1" ]]; then
    echo "$USAGE"
    exit 1
fi

if [[ -r "$param_val" ]]; then
    while read line; do
	echo "$counter:$line"
	((counter=counter+1))
    done < $param_val
else
    echo "$ERROR"
    exit 1
fi

exit 0



