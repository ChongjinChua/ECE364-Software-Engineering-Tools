!/bin/bash

#$Author: ee364g13 $
#$Date: 2016-02-24 15:22:27 -0500 (Wed, 24 Feb 2016) $
#$Revisions$
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364g13/Prelab02/yards.bash $
#$Id: yards.bash 88866 2016-02-24 20:22:27Z ee364g13 $

param_num=$#
param_val=$@
USAGE="Usage: yards.bash <filename>"
ERROR="Error: $param_val is not readable"

#ONLY ALLOWS 1 ARGUMENT
if (($param_num != 1)); then
    echo "$USAGE"
    exit 1
elif [[ ! -e $param_val && ! -r $param_val ]]; then
    echo "$ERROR"
    exit 1
fi

let count=0
while read line; do
    let sum=0

    conference_name=$(echo $line | cut -d' ' -f1)
    Arr=($(echo $line | cut -d' ' -f2-))

    for I in ${Arr[*]}; do
	(( sum=$sum+$I ))
    done
    (( avg=$sum/${#Arr[*]} ))

    A_avg[$count]=$avg

    let temp=0
    for I in ${Arr[*]}; do
	(( temp=$temp+($I-$avg)**2 ))
    done
    
    (( var=$temp/${#Arr[*]} ))

    (( count++ ))

    echo "$conference_name schools averaged $avg yards receiving with a variance of $var"
done <$param_val

let highest_avg=0
for I in ${A_avg[*]}; do
    if (( $I > $highest_avg )); then
	highest_avg=$I
    fi
done

echo "The largest average yardage was $highest_avg"

exit 0
