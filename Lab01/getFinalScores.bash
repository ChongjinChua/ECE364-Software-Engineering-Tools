#! /bin/bash
#
#$Author: ee364g13 $
#$Date: 2016-01-20 15:14:23 -0500 (Wed, 20 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364g13/Lab01/getFinalScores.bash $
#$Revision: 86388 $
#$Id: getFinalScores.bash 86388 2016-01-20 20:14:23Z ee364g13 $

param_num=$#
param_val=$@
param_val_out=$(echo $param_val | cut -d'/' -f2 | cut -d'.' -f1)
USAGE="Usage: getFinalScores.bash <filename>" #return code 1
ERROR_NEXIST="Error reading input file: $param_val"  #return code 2
ERROR_EXIST="Output file gradebooks/$param_val_out.out already exists."  #return code 3

if (($param_num != 1)); then
    echo "$USAGE"
    exit 1
elif [[ ! -e $param_val ]]; then
    echo "$ERROR_NEXIST"
    exit 2
elif [[ -e ./gradebooks/$param_val_out.out ]]; then
    echo "$ERROR_EXIST"
    exit 3
fi

touch ./gradebooks/$param_val_out.out

let final_score=0
while read -u 3 -r line; do

    (( final_score=15*$(echo $line | cut -d',' -f2)/100+30*$(echo $line | cut -d',' -f3)/100+30*$(echo $line | cut -d',' -f4)/100+25*$(echo $line | cut -d',' -f5)/100 ))

    echo "$(echo $line | cut -d',' -f1),$final_score" >> ./gradebooks/$param_val_out.out

    final_score=0
done 3<$param_val

exit 0

