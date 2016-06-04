#! /usr/bin/env python3.4
import re

def getAddress(sentence):
    regex = r"([A-Fa-f0-9]{2}[\:\-]{1}){5}[A-Fa-f0-9]{2}"
    result = re.search(regex,sentence)
    if result:
        return result.group()
    else:
        return None

def getSwitches(commandline):
    regex = r"[+\\][a-z][ ]+[\w\/\.\:]+"
    regex2 = r"[\w\/\.\:]+"
    result = re.findall(regex,commandline)
    return_lst = []
    if result:
        for item in result:
            final_result = re.findall(regex2,item)
            return_lst.append((final_result[0],final_result[1]))
        return_lst.sort()
        return return_lst
    else:
        return None
    
def getElements(fullAddress):
    regex = r"^(http://|https://)([A-Za-z0-9\.]+)/([A-Za-z0-9]+)/([A-Za-z0-9]+$)"
    result = re.search(regex,fullAddress)
    if result:
        lst = [result.group(2),result.group(3),result.group(4)]
        return tuple(lst)
    else:
        print(None)


if __name__ == "__main__":
    #print(getAddress("The card was at 58-1c-0a-6e-39-4d, but it was removed."))
    #getSwitches(r"myScript.bash +v  \i 2   +p  /local/bin/somefolder")
    getElements("https://www.paypal.com/Customer1Area/Pay2")
    pass


