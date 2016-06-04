#! /usr/bin/env python3.4

#$Author: ee364g13 $
#$Date: 2016-02-20 02:27:34 -0500 (Sat, 20 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364g13/Prelab06/ip_detect.py $
#$Revision: 88479 $
#$Id: ip_detect.py 88479 2016-02-20 07:27:34Z ee364g13 $

import re
import sys

def ip_detection(filename):
    regex = r"(?<=:)\d+$"

    with open(filename,'r') as fptr:
        all_lines = fptr.readlines()
    for line in all_lines:
        valid_num = re.search(r"(?<!\S)(((2[0-5][0-5])?|(1[0-9][0-9])?|(0?[0-9]?[0-9]))(\.|\:)){4}",line)
            
        if valid_num:
            result = re.search(regex,line)
            if result:
                if int(result.group(0)) < 1024:
                    print(line.strip() + " - Valid (root privileges required)")
                elif int(result.group(0)) > 32767:
                    print(line.strip() + " - Invalid Port Number")
                else:
                    print(line.strip() + " - Valid")
            else:
                print(line.strip() + " - Invalid Port Number")
        else:
            print(line.strip() + " - Invalid IP Address")

    pass

if __name__ == "__main__":

    ip_detection(sys.argv[1])
    pass
