#! /usr/bin/env python3.4

#$Author: ee364g13 $
#$Date: 2016-02-22 15:56:50 -0500 (Mon, 22 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364g13/Prelab06/function_finder.py $
#$Revision: 88573 $
#$Id: function_finder.py 88573 2016-02-22 20:56:50Z ee364g13 $

import re
import os, sys


def find_function(filename):
    regex = r"def[ ]+(?P<func_name>[A-Za-z][\w-]*)[ ]*\((?P<alpha>([\d\w *\=\-\,]\,?){0,})\):"
    with open(filename, 'r') as fptr:
        all_lines = fptr.readlines()
    for line in all_lines:
        searched = re.search(regex,line)
        if searched:
            #print("alpha = {0}".format(searched.group("alpha")))
            #print("func_name = {0}".format(searched.group("func_name")))

            arg_list = searched.group("alpha").split(',')
            print(searched.group("func_name"))
            count = 1
            for item in arg_list:
                print("Arg{0}: {1}".format(count,item.strip()))
                count += 1
                  
    pass



if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: function_finder.py [python_file_name]")
    else:
        valid = os.access(sys.argv[1],os.R_OK)
        if valid is False:
            print("Error: Could not read {0}".format(sys.argv[1]))
        else:
            find_function(sys.argv[1])

    pass
