
#!/bin/bash

#$Author: ee364g13 $
#$Date: 2016-01-16 23:55:42 -0500 (Sat, 16 Jan 2016) $
#$Revisions$
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364g13/Prelab01/check_file.bash $
#$Id: check_file.bash 85235 2016-01-17 04:55:42Z ee364g13 $

param_num=$#
param_val=$@
USAGE="Usage: ./check_file.bash <filename>"
ERROR=""

if [[ "$param_num" != "1" ]]; then
    echo "$USAGE"
    exit 1
fi

if [[ -e "$param_val" ]]; then
    ERROR=""
else
    ERROR=" does not"
fi
echo "$param_val$ERROR exists"

if [[ -d "$param_val" ]]; then
    ERROR=""
else
    ERROR=" not"
fi
echo "$param_val is$ERROR a directory"

if [[ -f "$param_val" ]]; then
    ERROR=""
else
    ERROR=" not"
fi
echo "$param_val is$ERROR an ordinary file"

if [[ -r "$param_val" ]]; then
    ERROR=""
else
    ERROR=" not"
fi
echo "$param_val is$ERROR readable"

if [[ -w "$param_val" ]]; then
    ERROR=""
else
    ERROR=" not"
fi
echo "$param_val is$ERROR writable"

if [[ -x "$param_val" ]]; then
    ERROR=""
else
    ERROR=" not"
fi
echo "$param_val is$ERROR executable"

exit 0



