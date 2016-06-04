#$Author: ee364g13 $
#$Date: 2016-02-12 20:41:26 -0500 (Fri, 12 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364g13/Lab04/registrar.py $
#$Revision: 88192 $
#$Id: registrar.py 88192 2016-02-13 01:41:26Z ee364g13 $

import glob
from pprint import pprint as pp

def getDetails():
    dict_stu = {}
    dict_course = {}
    stu_file = "./files/students.txt"
    with open(stu_file,'r') as stu_file_ptr:
        all_lines = stu_file_ptr.readlines()
    for line in all_lines[2:]:
        line = line.split('|')
        dict_stu[line[1].strip()] = str(line[0].strip())

    all_files = glob.glob('./files/EE*')
    for file in all_files:
        with open(file,'r') as file_ptr:
            all_lines = file_ptr.readlines()
        for line in all_lines[2:]:
            line = line.split()
            sid = line[0].strip()
            item = [file[12:15],round(float(line[1].strip()))]
            if sid not in dict_course.keys():
                dict_course[sid] = [tuple(item)]
            else:
                dict_course[sid].append(tuple(item))

    for item in dict_stu.keys():
        dict_course[dict_stu[item]] = set(dict_course.pop(item))

    return dict_course

def getStudentList(classNumber):
    temp_list = []
    return_list = []
    dict_stu = {}
    all_files = glob.glob('./files/EE*')
    all_files_clean = [file[12:15] for file in all_files]

    stu_file = "./files/students.txt"
    with open(stu_file,'r') as stu_file_ptr:
        all_lines = stu_file_ptr.readlines()
    for line in all_lines[2:]:
        line = line.split('|')
        dict_stu[line[1].strip()] = str(line[0].strip())

    if classNumber not in all_files_clean:
        return temp_list
    else:
        with open("./files/EECS"+classNumber+".txt",'r') as ptr:
            all_lines = ptr.readlines()
        for line in all_lines[2:]:
            line = line.split()
            temp_list.append(line[0].strip())

    for item in temp_list:
        return_list.append(dict_stu[item])

    return_list.sort()

    return return_list

def searchForName(studentName):
    dict_stu = {}
    dict_return = {}
    stu_file = "./files/students.txt"
    with open(stu_file,'r') as stu_file_ptr:
        all_lines = stu_file_ptr.readlines()
    for line in all_lines[2:]:
        line = line.split('|')
        dict_stu[line[1].strip()] = str(line[0].strip())
    
    if studentName not in dict_stu.values():
        return {}
    else:
        dict_full = getDetails()
        for x, y in dict_full.get(studentName):
            dict_return[x] = y

    return dict_return

def searchForID(studentID):
    dict_stu = {}
    dict_return = {}
    stu_file = "./files/students.txt"
    with open(stu_file,'r') as stu_file_ptr:
        all_lines = stu_file_ptr.readlines()
    for line in all_lines[2:]:
        line = line.split('|')
        dict_stu[line[1].strip()] = str(line[0].strip())
    
    if studentID not in dict_stu.keys():
        return {}
    else:
        studentName = dict_stu.get(studentID)
        dict_full = getDetails()
        for x, y in dict_full.get(studentName):
            dict_return[x] = y

    return dict_return    

def findScore(studentName, classNumber):
    dict_full = getDetails()
    dict_new = {}
    if studentName not in dict_full.keys():
        return None

    for item in dict_full[studentName]:
        x, y = item
        dict_new[x] = y

    if classNumber not in dict_new.keys():
        return None
    else:
        return dict_new[classNumber]

def getHighest(classNumber):
    dict_stu = {}
    stu_file = "./files/students.txt"
    with open(stu_file,'r') as stu_file_ptr:
        all_lines = stu_file_ptr.readlines()
    for line in all_lines[2:]:
        line = line.split('|')
        dict_stu[line[1].strip()] = str(line[0].strip())

    dict_new = {}

    all_files = glob.glob('./files/EE*')
    all_files_clean = [file[12:15] for file in all_files]
    if classNumber not in all_files_clean:
        return ()
    else:
        with open("./files/EECS"+classNumber+".txt",'r') as ptr:
            all_lines = ptr.readlines()
        #max_val = max(all_lines[2:].split()[1])
        for line in all_lines[2:]:
            line = line.split()
            dict_new[round(float(line[1]))] = line[0]

    max_val = max(dict_new.keys())
    x = [dict_stu[dict_new[max_val]],max_val]
    
    return tuple(x)

def getLowest(classNumber):
    dict_stu = {}
    stu_file = "./files/students.txt"
    with open(stu_file,'r') as stu_file_ptr:
        all_lines = stu_file_ptr.readlines()
    for line in all_lines[2:]:
        line = line.split('|')
        dict_stu[line[1].strip()] = str(line[0].strip())

    dict_new = {}

    all_files = glob.glob('./files/EE*')
    all_files_clean = [file[12:15] for file in all_files]
    if classNumber not in all_files_clean:
        return ()
    else:
        with open("./files/EECS"+classNumber+".txt",'r') as ptr:
            all_lines = ptr.readlines()
        #max_val = max(all_lines[2:].split()[1])
        for line in all_lines[2:]:
            line = line.split()
            dict_new[round(float(line[1]))] = line[0]

    min_val = min(dict_new.keys())
    x = [dict_stu[dict_new[min_val]],min_val]

    return tuple(x)

def getAverageScore(studentName):
    dict_stu = getDetails()
    avg = 0
    count = 0
    if studentName not in dict_stu.keys():
        return None
    else:
        for x,y in dict_stu[studentName]:
            avg += y
            count += 1
    return avg/count

if __name__ == "__main__":
    #getDetails();
    #print(getStudentList("370"))
    #print(searchForName('Joyce Q Kelly'))
    #print(findScore('Arya Stark','370'))
    print(getHighest('370'))
    pass
