import re
from pprint import pprint as pp

def getRejectedUsers():
    #a=re.search(        r"(?P<names>([A-Za-z]+ [A-Za-z]+)|([A-Za-z]+[, ]{2}?[A-Za-z]+)([,; ]+)(?P<email>[\w\.-]+@[\w\.-]+)?([,; ]+)(?P<hp_num>([\d\(\)-]+)|(\(\d{3}\) \d{3}-\d{4}))?([,; ]+)(?P<state>([\w]+)|(\w+ \w+))?")
    regex = r"(?P<names>([A-Za-z]+ [A-Za-z]+)|([A-Za-z]+[, ]{2}?[A-Za-z]+))([,; ]+)(?P<email>[\w\.-]+@[\w\.-]+)?([,; ]+)(?P<hp_num>([\d\(\)-]+)|(\(\d{3}\) \d{3}-\d{4}))?([,; ]+)(?P<state>([\w]+)|(\w+ \w+))?"
    regex_name_firlas = r"(?P<fir>[\w]+) (?P<las>[\w]+)"
    regex_name_lasfir = r"(?P<las>[\w]+), (?P<fir>[\w]+)"
    baduser = []
    with open("SiteRegistration.txt",'r') as fptr:
        all_lines = fptr.readlines()
    for line in all_lines:
        m = re.search(regex,line)
        if m:
            #print(m.group("names"))
            firlas = re.search(regex_name_firlas,m.group("names"))
            lasfir = re.search(regex_name_lasfir,m.group("names"))
            if m.group("email") is None and m.group("hp_num") is None and m.group("state") is None:
                if firlas:
                    str_name = firlas.group("fir") + " " + firlas.group("las")
                    baduser.append(str_name)
                else:
                    str_name = lasfir.group("fir") + " " + lasfir.group("las")
                    baduser.append(str_name)
        else:
            print("error in regex")
    baduser.sort()
    #print(baduser)
    return baduser
    
def getUsersWithEmails():
    dict = {}
    regex = r"(?P<names>([A-Za-z]+ [A-Za-z]+)|([A-Za-z]+[, ]{2}?[A-Za-z]+))([,; ]+)(?P<email>[\w\.-]+@[\w\.-]+)?([,; ]+)(?P<hp_num>([\d\(\)-]+)|(\(\d{3}\) \d{3}-\d{4}))?([,; ]+)(?P<state>([\w]+)|(\w+ \w+))?"
    regex_name_firlas = r"(?P<fir>[\w]+) (?P<las>[\w]+)"
    regex_name_lasfir = r"(?P<las>[\w]+), (?P<fir>[\w]+)"
    baduser = []
    with open("SiteRegistration.txt",'r') as fptr:
        all_lines = fptr.readlines()
    for line in all_lines:
        m = re.search(regex,line)
        if m:
            firlas = re.search(regex_name_firlas,m.group("names"))
            lasfir = re.search(regex_name_lasfir,m.group("names"))
            if m.group("email") is not None:
                if firlas:
                    str_name = firlas.group("fir") + " " + firlas.group("las")
                    dict[str_name] = m.group("email")
                else:
                    str_name = lasfir.group("fir") + " " + lasfir.group("las")
                    dict[str_name] = m.group("email")
        else:
            print("error in regex")

    return dict
    

def getUsersWithPhones():
    dict = {}
    regex = r"(?P<names>([A-Za-z]+ [A-Za-z]+)|([A-Za-z]+[, ]{2}?[A-Za-z]+))([,; ]+)(?P<email>[\w\.-]+@[\w\.-]+)?([,; ]+)(?P<hp_num>(\(\d{3}\) \d{3}-\d{4})|(\d{3}-?\d{3}-?\d{4}))?([,; ]+)(?P<state>([\w]+)|(\w+ \w+))?"
    regex_name_firlas = r"(?P<fir>[\w]+) (?P<las>[\w]+)"
    regex_name_lasfir = r"(?P<las>[\w]+), (?P<fir>[\w]+)"
    with open("SiteRegistration.txt",'r') as fptr:
        all_lines = fptr.readlines()
    for line in all_lines:
        m = re.search(regex,line)
        if m:
            firlas = re.search(regex_name_firlas,m.group("names"))
            lasfir = re.search(regex_name_lasfir,m.group("names"))
            if m.group("hp_num") is not None:
                str_hp = ""
                for i in m.group("hp_num"):
                    if i.isdigit():
                        str_hp += str(i)
                if firlas:
                    str_name = firlas.group("fir") + " " + firlas.group("las")
                    str_hp = "(" + str_hp[0:3] + ")" + " " + str_hp[3:6] + "-" + str_hp[6:]
                    dict[str_name] = str_hp
                else:
                    str_name = lasfir.group("fir") + " " + lasfir.group("las")
                    str_hp = "(" + str_hp[0:3] + ")" + " " + str_hp[3:6] + "-" + str_hp[6:]
                    dict[str_name] = str_hp
        else:
            print("error in regex")

    return dict

def getUsersWithStates():
    dict = {}
    regex = r"(?P<names>([A-Za-z]+ [A-Za-z]+)|([A-Za-z]+[, ]{2}?[A-Za-z]+))([,; ]+)(?P<email>[\w\.-]+@[\w\.-]+)?([,; ]+)(?P<hp_num>(\(\d{3}\) \d{3}-\d{4})|(\d{3}-?\d{3}-?\d{4}))?([,; ]+)(?P<state>([A-Za-z]+$)|([A-Za-z]+ [A-Za-z]+))?"
    regex_name_firlas = r"(?P<fir>[\w]+) (?P<las>[\w]+)"
    regex_name_lasfir = r"(?P<las>[\w]+), (?P<fir>[\w]+)"
    with open("SiteRegistration.txt",'r') as fptr:
        all_lines = fptr.readlines()
    for line in all_lines:
        m = re.search(regex,line)
        if m:
            firlas = re.search(regex_name_firlas,m.group("names"))
            lasfir = re.search(regex_name_lasfir,m.group("names"))
            if m.group("state") is not None:
                if firlas:
                    str_name = firlas.group("fir") + " " + firlas.group("las")
                    dict[str_name] = m.group("state")
                else:
                    str_name = lasfir.group("fir") + " " + lasfir.group("las")
                    dict[str_name] = m.group("state")
        else:
            print("error in regex")
    pp(dict)
    return dict

def getUsersWithoutEmails():
    rtn_list = []
    regex = r"(?P<names>([A-Za-z]+ [A-Za-z]+)|([A-Za-z]+[, ]{2}?[A-Za-z]+))([,; ]+)(?P<email>[\w\.-]+@[\w\.-]+)?([,; ]+)(?P<hp_num>(\(\d{3}\) \d{3}-\d{4})|(\d{3}-?\d{3}-?\d{4}))?([,; ]+)(?P<state>([A-Za-z]+$)|([A-Za-z]+ [A-Za-z]+))?"
    regex_name_firlas = r"(?P<fir>[\w]+) (?P<las>[\w]+)"
    regex_name_lasfir = r"(?P<las>[\w]+), (?P<fir>[\w]+)"
    with open("SiteRegistration.txt",'r') as fptr:
        all_lines = fptr.readlines()
    for line in all_lines:
        m = re.search(regex,line)
        if m:
            firlas = re.search(regex_name_firlas,m.group("names"))
            lasfir = re.search(regex_name_lasfir,m.group("names"))            
            if m.group("email") is None:
                if m.group("hp_num") is not None:
                    if firlas:
                        str_name = firlas.group("fir") + " " + firlas.group("las")
                        rtn_list.append(str_name)
                    else:
                        str_name = lasfir.group("fir") + " " + lasfir.group("las")
                        rtn_list.append(str_name)
                elif m.group("state") is not None:
                    if firlas:
                        str_name = firlas.group("fir") + " " + firlas.group("las")
                        rtn_list.append(str_name)
                    else:
                        str_name = lasfir.group("fir") + " " + lasfir.group("las")
                        rtn_list.append(str_name)
        else:
            print("error in regex")

    rtn_list.sort()
    return rtn_list;

def getUsersWithoutPhones():
    rtn_list = []
    regex = r"(?P<names>([A-Za-z]+ [A-Za-z]+)|([A-Za-z]+[, ]{2}?[A-Za-z]+))([,; ]+)(?P<email>[\w\.-]+@[\w\.-]+)?([,; ]+)(?P<hp_num>(\(\d{3}\) \d{3}-\d{4})|(\d{3}-?\d{3}-?\d{4}))?([,; ]+)(?P<state>([A-Za-z]+$)|([A-Za-z]+ [A-Za-z]+))?"
    regex_name_firlas = r"(?P<fir>[\w]+) (?P<las>[\w]+)"
    regex_name_lasfir = r"(?P<las>[\w]+), (?P<fir>[\w]+)"
    with open("SiteRegistration.txt",'r') as fptr:
        all_lines = fptr.readlines()
    for line in all_lines:
        m = re.search(regex,line)
        if m:
            firlas = re.search(regex_name_firlas,m.group("names"))
            lasfir = re.search(regex_name_lasfir,m.group("names"))            
            if m.group("hp_num") is None:
                if m.group("state") is not None:
                    if firlas:
                        str_name = firlas.group("fir") + " " + firlas.group("las")
                        rtn_list.append(str_name)
                    else:
                        str_name = lasfir.group("fir") + " " + lasfir.group("las")
                        rtn_list.append(str_name)
                elif m.group("email") is not None:
                    if firlas:
                        str_name = firlas.group("fir") + " " + firlas.group("las")
                        rtn_list.append(str_name)
                    else:
                        str_name = lasfir.group("fir") + " " + lasfir.group("las")
                        rtn_list.append(str_name)
        else:
            print("error in regex")

    rtn_list.sort()
    return rtn_list;

def getUsersWithoutStates():
    rtn_list = []
    regex = r"(?P<names>([A-Za-z]+ [A-Za-z]+)|([A-Za-z]+[, ]{2}?[A-Za-z]+))([,; ]+)(?P<email>[\w\.-]+@[\w\.-]+)?([,; ]+)(?P<hp_num>(\(\d{3}\) \d{3}-\d{4})|(\d{3}-?\d{3}-?\d{4}))?([,; ]+)(?P<state>([A-Za-z]+$)|([A-Za-z]+ [A-Za-z]+))?"
    regex_name_firlas = r"(?P<fir>[\w]+) (?P<las>[\w]+)"
    regex_name_lasfir = r"(?P<las>[\w]+), (?P<fir>[\w]+)"
    with open("SiteRegistration.txt",'r') as fptr:
        all_lines = fptr.readlines()
    for line in all_lines:
        m = re.search(regex,line)
        if m:
            firlas = re.search(regex_name_firlas,m.group("names"))
            lasfir = re.search(regex_name_lasfir,m.group("names"))            
            if m.group("state") is None:
                if m.group("hp_num") is not None:
                    if firlas:
                        str_name = firlas.group("fir") + " " + firlas.group("las")
                        rtn_list.append(str_name)
                    else:
                        str_name = lasfir.group("fir") + " " + lasfir.group("las")
                        rtn_list.append(str_name)
                elif m.group("email") is not None:
                    if firlas:
                        str_name = firlas.group("fir") + " " + firlas.group("las")
                        rtn_list.append(str_name)
                    else:
                        str_name = lasfir.group("fir") + " " + lasfir.group("las")
                        rtn_list.append(str_name)
        else:
            print("error in regex")

    rtn_list.sort()
    return rtn_list;

def getUsersWithCompleteInfo():
    dict = {}
    rtn_list = []
    regex = r"(?P<names>([A-Za-z]+ [A-Za-z]+)|([A-Za-z]+[, ]{2}?[A-Za-z]+))([,; ]+)(?P<email>[\w\.-]+@[\w\.-]+)?([,; ]+)(?P<hp_num>(\(\d{3}\) \d{3}-\d{4})|(\d{3}-?\d{3}-?\d{4}))?([,; ]+)(?P<state>([A-Za-z]+$)|([A-Za-z]+ [A-Za-z]+))?"
    regex_name_firlas = r"(?P<fir>[\w]+) (?P<las>[\w]+)"
    regex_name_lasfir = r"(?P<las>[\w]+), (?P<fir>[\w]+)"
    with open("SiteRegistration.txt",'r') as fptr:
        all_lines = fptr.readlines()
    for line in all_lines:
        m = re.search(regex,line)
        if m:
            firlas = re.search(regex_name_firlas,m.group("names"))
            lasfir = re.search(regex_name_lasfir,m.group("names"))
            if m.group("state") is not None and m.group("hp_num") is not None and m.group("email") is not None:
                str_hp = ""
                for i in m.group("hp_num"):
                    if i.isdigit():
                        str_hp += str(i)
                if firlas:
                    str_name = firlas.group("fir") + " " + firlas.group("las")
                else:
                    str_name = lasfir.group("fir") + " " + lasfir.group("las")
                str_hp = "(" + str_hp[0:3] + ")" + " " + str_hp[3:6] + "-" + str_hp[6:]
                rtn_list.append(m.group("email"))
                rtn_list.append(str_hp)
                rtn_list.append(m.group("state"))
                rtn_tuple = tuple(rtn_list)
                dict[str_name] = rtn_tuple
                rtn_list = []

        else:
            print("error in regex")

    return dict;

    
if __name__ == "__main__":
    #getRejectedUsers()
    #getUsersWithEmails()
    #getUsersWithPhones()
    #getUsersWithStates()
    #getUsersWithCompleteInfo()
    pass
