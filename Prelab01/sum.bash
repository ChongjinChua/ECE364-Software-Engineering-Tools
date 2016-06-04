#!/bin/bash

#$Author: ee364g13 $
#$Date: 2016-01-17 11:36:15 -0500 (Sun, 17 Jan 2016) $
#$Revisions$
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364g13/Prelab01/sum.bash $
#$Id: sum.bash 85297 2016-01-17 16:36:15Z ee364g13 $

param_num=$#;
let sum=0;

while (("$#")); do

    ((sum=sum+"$1"));

shift

done

echo ${sum}

exit 0



