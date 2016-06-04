#$Author: ee364g13 $
#$Date: 2016-02-20 02:27:34 -0500 (Sat, 20 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364g13/Prelab06/email.py $
#$Revision: 88479 $
#$Id: email.py 88479 2016-02-20 07:27:34Z ee364g13 $

import re


def email():
    filename = "Part2.in"
    email_regex = r"([\w]+)@([\w.]+)"
    score_regex = r"((?<!\S)[\d.]+)"
    with open(filename,'r') as fptr:
        all_lines = fptr.readlines()
    for line in all_lines:
        email_result = re.search(email_regex,line)
        score_result = re.search(score_regex,line)        
        output_str = email_result.group(1) + "@"
        if len(email_result.group(1)) < 5:
            format_str = "\t\t"
        else:
            format_str = "\t"
        score_str = format_str + score_result.group(0) + "/100"
        if email_result.group(2)[0:3] == "pur":
            output_str += "ecn."

        output_str += email_result.group(2)
        output_str += score_str
        print(output_str)
    
    pass
    
if __name__ == "__main__":
    
    email()
    pass
