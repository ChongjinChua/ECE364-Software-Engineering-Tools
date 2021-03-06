#! /bin/bash
#
#$Author: ee364g13 $
#$Date: 2016-01-25 14:01:34 -0500 (Mon, 25 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364g13/Lab01/getCourseStats.bash $
#$Revision: 86727 $
#$Id: getCourseStats.bash 86727 2016-01-25 19:01:34Z ee364g13 $

param_num=$#
param_val=$@
USAGE="Usage: ./getCourseStats.bash <course name>" #return code 1
ERROR_NEXIST="Error: course $param_val is not a valid option"  #return code 5
ERROR_GFS="Error whlie running getFinalScores.bash"  #return code 3

if (($param_num != 1)); then
    echo "$USAGE"
    exit 1
elif [[ "$param_val" != "ece364" && "$param_val" != "ece337" && "$param_val" != "ece468" ]]; then
    echo $param_val
    echo "$ERROR_NEXIST"
    exit 5
fi

let stu_num=0
let stu_avg=0
let avg_hold=0
let stu_line=0
let highest_score=0
let highest_stu=0
let section_count=0

for I in gradebooks/"$param_val"_section*.txt; do
        
    ./getFinalScores.bash ${I}
    if (( $? != 0 )); then
	echo "$ERROR_GFS"
	exit 3
    fi
    J=$(echo ${I} | cut -d'.' -f1).out
    stu_line=$(wc -l $J | cut -d' ' -f1)
    (( stu_num=stu_num+stu_line ))
    while read line; do
	avg_hold=$(echo $line | cut -d',' -f2)
	name_hold=$(echo $line | cut -d',' -f1)
	(( stu_avg=stu_avg+avg_hold ))
	if (( $avg_hold > $highest_score )); then
	    (( highest_score=avg_hold ))
	    highest_stu=$name_hold
	fi
    done <$J

done

(( stu_avg=stu_avg/stu_num ))
echo "Total students: $stu_num"
echo "Average score: $stu_avg" 
echo "$highest_stu had the highest score of $highest_score"

exit 0

