#$Author
#$Date
#$HeadURL
#$Revision
#$Id

import glob
from pprint import pprint as pp

def getWordFrequency():
    dictionary = {}
    all_files = glob.glob('./files/*.txt')
    for files_lcv in all_files:
        with open(files_lcv,'r') as file_ut:
            all_lines = file_ut.readlines()
        for line_lcv in all_lines:
            for word_lcv in line_lcv.split():
                word_lcv = stripPunctuations(word_lcv)
                if word_lcv not in dictionary.keys():
                    dictionary[word_lcv] = 1
                else:
                    dictionary[word_lcv] += 1
    return dictionary

def stripPunctuations(item):
    if type(item) is list:
        new_list = []
        for i in item:
            if '.' in i:
                i = i[:-1]
            elif ',' in i:
                i = i[:-1]
            new_list.append(i)
        return new_list
    else:
        if '.' in item:
            return item[:-1]
        elif ',' in item:
            return item[:-1]
        else:
            return item

def getDuplicates():
    dictionary = {}
    all_files = glob.glob('./files/*.txt')
    for files_lcv in all_files:
        similar_flag = 0
        with open(files_lcv,'r') as file_ut:
            raw_all_lines = file_ut.readlines()

        for dict_key_lcv in dictionary.keys():
            with open(makeFileFormat(dict_key_lcv),'r') as dict_file_ut:
                dict_all_lines = dict_file_ut.readlines()
            if dict_all_lines == raw_all_lines:
                similar_flag = 1
                break

        files_lcv = makeFileFormat(files_lcv)

        if similar_flag == 0:
            one_big_list = []
            for line_i in raw_all_lines:
                one_big_list += line_i.split()

            one_big_list = stripPunctuations(one_big_list)
            word_count = len(set(one_big_list))
            dictionary[files_lcv] = [word_count, [files_lcv]]

        else:
            dict_val = dictionary.get(dict_key_lcv)
            dict_val[1].append(files_lcv)
            dict_val[1].sort()
            new_key = dict_val[1][0]
            dictionary[dict_key_lcv] = dict_val
            dictionary[new_key] = dictionary.pop(dict_key_lcv)
                
    for item in dictionary.keys():
        dictionary[item] = tuple(dictionary[item])
    return dictionary


def makeFileFormat(filename):
    if filename[0] == '.':
        return filename[8:11]
    else:
        return './files/' + filename + '.txt'
    pass
    
def getPurchaseReport():
    dict_itemList = {}
    dict_totalCost = {}
    itemList_file = glob.glob('./purchases/Item List*')
    all_files = glob.glob('./purchases/p*.txt')
    
    with open(itemList_file[0],'r') as item_file_ptr:
        all_lines = item_file_ptr.readlines()

    all_lines = all_lines[2:]
    for item in all_lines:
        key = item.split()[0]
        value = item.split()[1]
        dict_itemList[key] = float(value[1:])

    for single_file in all_files:
        cost = 0
        with open(single_file, 'r') as file_ptr:
            all_lines = file_ptr.readlines()
        all_lines = all_lines[2:]
        for item in all_lines:
            cost += dict_itemList.get(item.split()[0]) * float(item.split()[1])
        dict_totalCost[int(single_file[21:24])] = round(cost,2)
    return dict_totalCost

def getTotalSold():
    dict_itemQuantity = {}
    all_files = glob.glob('./purchases/p*.txt')
    for single_file in all_files:
        with open(single_file, 'r') as file_ptr:
            all_lines = file_ptr.readlines()
        all_lines = all_lines[2:]
        for item in all_lines:
            key = str(item.split()[0])
            value = int(item.split()[1])
            if key in dict_itemQuantity.keys():
                dict_itemQuantity[key] += value
            else:
                dict_itemQuantity[key] = value
                
    return dict_itemQuantity

if __name__ == "__main__":
    #pp(getWordFrequency())
    #pp(getDuplicates())
    #getDuplicates()
    #pp(getPurchaseReport())
    #pp(getTotalSold())
    pass
    



    
