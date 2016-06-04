#! /usr/bin/env python3.4
import re, math

def idIsAcceptable(ver_id):
    regex = r"^[A-Za-z0-9_]+$"
    if re.search(regex,ver_id):
        return True
    else:
        return False
    
def processSingle(ver_assignment):
    regex = r"^\.(?P<portname>[\S]+)\((?P<pinname>[\S]+)\)$"
    result = re.search(regex,ver_assignment)

    if result:
        port_name = result.group("portname")
        pin_name = result.group("pinname")        
        if idIsAcceptable(port_name) and idIsAcceptable(pin_name):
            return tuple([port_name,pin_name])

    raise ValueError(ver_assignment)
    
    pass

def processLine(ver_line):
    error_str = ver_line
    regex = r"[ ]*(?P<comp>[\S]+)[ ]+(?P<instance>[\S]+)[ ]*\([ ]*(?P<assignment>\.[\S\s]+)[ ]*\)$"
    result = re.search(regex,ver_line)
    #print(ver_line)
    #print(result.group("comp"))
    #print(result.group("instance"))
    #print(result.group("assignment"))
    
    if result:
        #print(result)
        regex_a = "(?P<single>^\.[\S\s]+\)$)"
        comp_name = result.group("comp")
        instance_name = result.group("instance")
        assignment_name = result.group("assignment").strip()
        singles = re.search(regex_a,assignment_name)
        singles_iter = singles.group().split(',')
        single_list = []

        for item in singles_iter:
            rtn_tup = processSingle(item.strip())
            if rtn_tup:
                single_list.append(rtn_tup)
            else:
                raise ValueError(item)

        if idIsAcceptable(comp_name) and idIsAcceptable(instance_name):
            return tuple([comp_name,instance_name,tuple(single_list)])
        else:
            error_str = assignment_name

    raise ValueError(error_str)
    
    pass
    

if __name__ == "__main__":
    pass
