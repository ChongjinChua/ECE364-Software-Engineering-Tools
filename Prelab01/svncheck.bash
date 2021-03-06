#!/bin/bash

#$Author: ee364g13 $
#$Date: 2016-01-18 23:33:13 -0500 (Mon, 18 Jan 2016) $
#$Revisions$
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364g13/Prelab01/svncheck.bash $
#$Id: svncheck.bash 86080 2016-01-19 04:33:13Z ee364g13 $

param_num=$#
param_val=$@
USAGE="Usage: ./svncheck.bash <filename>"

#ONLY ALLOWS 1 ARGUMENT
if (($param_num != 1)); then
    echo "$USAGE"
    exit 1
fi

while read -u 3 -r line; do

    status=$(svn status $line | cut -c1)

    if [[ "$status" == "" ]]; then #IT'S IN SVN REPO,
	if [[ -e $line && ! -x $line ]]; then
	    svn propset svn:executable ON $line

	elif [[ ! -e $line ]]; then #IF DOESN'T EXISTS
	    echo "Error: File "$line" appears to not exist here or in svn"

	fi

    elif [[ "$status" == "?" || "$status" == "M" || "$status" == "A" ]]; then #NOT IN SVN REPO,'?','A','M'
	if [[ -e $line ]]; then #IF EXISTS
	    #IF NOT EXECUTABLE, CHMOD
	    ans="hellno"

	    if [[ ! -x $line ]]; then
		read -p "Would you like to make "$line" an executable? " ans;
		echo $ans
		#chmod +x "$line"
		[[ "$ans" == "y" ]] && chmod +x "$line"
	    fi

	fi
	#ADD TO SVN REPO
	[[ "$status" == "?" ]] && svn add $line
    fi

done 3<$param_val

svn commit -m "Auto-committing code"

exit 0



