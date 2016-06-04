#!/bin/bash

#$Author: ee364g13 $
#$Date: 2016-01-17 11:36:15 -0500 (Sun, 17 Jan 2016) $
#$Revisions$
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364g13/Prelab01/exist.bash $
#$Id: exist.bash 85297 2016-01-17 16:36:15Z ee364g13 $

param_num=$#;

while (("$#")); do

    if [[ -e "$1" ]]; then
	if [[ -r "$1" ]]; then
	    echo "File "$1" is readable!"
	fi
    else
	touch "$1"
    fi

shift

done

exit 0



