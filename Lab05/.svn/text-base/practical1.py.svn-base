import glob
from pprint import pprint as pp

def rowSumIsValid(mat):
    array_sum = []
    for J in mat:
        indv_sum = 0
        for I in J:
            indv_sum += I
        array_sum.append(indv_sum)

    comp = array_sum[0]
    for I in array_sum[1:]:
        if I != comp:
            return False
            
    return True

def columnSumIsValid(mat):
    array_sum = []
    count = 0
    for J in mat:
        ind = 0
        for I in J:
            if count == 0:
                array_sum.append(I)
            else:
                array_sum[ind] += I
                ind = ind + 1
        count = 1

    comp = array_sum[0]
    for I in array_sum[1:]:
        if I != comp:
            return False
            
    return True        

def magicSquareIsValid(filePath):
    with open(filePath,'r') as fptr:
        all_lines = fptr.readlines()
    mat = []

    for line in all_lines:
        single_list = []
        line = line.strip()
        for I in line.split():
            single_list.append(int(I))
        mat.append(single_list)

    if rowSumIsValid(mat) is False:
        return False
    elif columnSumIsValid(mat) is False:
        return False
    else:
        return True

def getTotalCost(itemSet):
    all_files = glob.glob('./Stores/*.txt')
    dict_list = [{},{},{},{},{}]
    new_dict_list = []
    return_dict = {}
    count = 0
    for file in all_files:
        with open(file,'r') as fptr:
            all_lines = fptr.readlines()
        filename = file.split('.')[1]
        filename = filename[8:]
        for line in all_lines[3:]:
            line = line.split(',')
            cpu = line[0].strip()
            price = line[1].strip()
            price = float(price[1:])
            dict_list[count][cpu] = price
        new_dict_list.append([filename,dict_list[count]])
        count += 1

    for cpu_name, quant in itemSet:
        for dict_item in new_dict_list:
            if cpu_name in dict_item[1].keys():
                product = quant * dict_item[1][cpu_name]
                #return_dict[dict_item[0]] += product
                if dict_item[0] in return_dict.keys():
                    return_dict[dict_item[0]] += round(product,2)
                else:
                    return_dict[dict_item[0]] = round(product,2)
    pp(return_dict)
    return return_dict
    
def getBestPrices(cpuSet):
    pass
def getMissingItems():
    pass

if __name__ == "__main__":
    #magicSquareIsValid("Squares/magic4.txt")
    getTotalCost({('Intel i7-4960HQ', 9), ('Intel i7-6700HQ', 7), ('Intel i7-6970HQ', 3)})
    
    pass
