import math

def getAverage(l):
    return recurse_helper(l,len(l)) / len(l)

def getHeadAverage(l, n):
    return recurse_helper(l, n) / n

def recurse_helper(l, n):
    if(n != 0):
        return l[0] + recurse_helper(l[1:],n-1)
    else:
        return 0    

def getTailMax(l, m):
    return getTailMax_helper(l[-(m-1):],m-1,l[0])
    
def getTailMax_helper(l, m, highest_num):
    if(m != 0):
        local_highest = getTailMax_helper(l[-(m-1):], m-1, l[0])
        if(highest_num > local_highest):
            return highest_num
        else:
            return local_highest
    else:
        return highest_num

def getNumberAverage(l):
    count = 0
    total = 0
    for item in l:
        if(type(item) is int):
            total += item
            count += 1
    return total / count

def getFormattedSSN(n):
    ssn_format = [3,2,4]
    n = str(n)[::-1]
    count = 0
    my_string = ""
    if(len(n) < 9):
        for item in range(9-len(n)):
            n += "0"
        n += n
    n = n[::-1]
    for I in ssn_format:
        I += count
        my_string += n[count:I]
        count = I
        my_string += "-"

    return my_string.rstrip("-")

def findName(l, s):
    ls = " " + s; rs = s + " "
    new_list = []
    for item in l:
        if(item.find(ls) != -1 or item.find(rs) != -1):
            new_list.append(item)
    return new_list

def getColumnSum(mat):
    if(len(mat) != 0):
        new_list = mat[0]
        for item_I in mat[1:]:
            index = 0
            for item_J in item_I:
                new_list[index] += item_J
                index += 1
        return new_list
    else:
        return 0

def getFormattedNames(ln):
    new_list = []
    for item in ln:
        new_string = item[2] + ", " + item[0] + " " + item[1] + "."
        new_list.append(new_string)
    return new_list

def getElementwiseSum(l1, l2):
    len_l1 = len(l1); len_l2 = len(l2)
    if(len_l1 < len_l2):
        a = [l1,l2[:len(l1)]]
        return getColumnSum(a) + l2[len(l1):]
    elif(len_l1 > len_l2):
        a = [l2,l1[:len(l2)]]        
        return getColumnSum(a) + l1[len(l2):]
    else:
        a = [l1,l2]
        return getColumnSum(a)

def removeDuplicates(l):
    occured = []
    return_l = []
    for item in l:
        if item not in occured[0:]:
            occured.append(item)
            return_l.append(item)
    return return_l

def getMaxOccurrence(l):
    dictionary = {}
    for item in l:
        dictionary[item] = l.count(item)
    return max(dictionary, key=dictionary.get)
    
    
if __name__ == "__main__":
    #print(getAverage([1,2,3,4,5,6,7,8]))
    #print(getHeadAverage([1,2,3,4,5,6,7,8],5))
    #print(getTailMax([1,2,3,4,5,6,7,8,0,9,3,2,341242,1,2,3],10))
    #print(getNumberAverage([1,2,3,"fdf",4,34.3,[8,9]]))
    #print(getFormattedSSN(12345))
    #print(findName(["John Smith","Aero Smith","hello", "Smithdf no"],"Smith"))
    #print(getColumnSum([[1,2,3],[1,2,3],[1,2,3],[1,2,3]]))
    #print(getFormattedNames([["George","W","Bush"],["Chong","J","Chua"]]))
    #print(getElementwiseSum([1,2,3],[1,2,3,4,5]))
    #print(getElementwiseSum([1,2,3,3,4,4,4,4],[1,2,3,4,5]))
    #print(getElementwiseSum([1,2,3],[1,2,3]))
    #print(removeDuplicates([1,2,2,3,4,4,4,4,3,6,7,8,8,8]))
    print(getMaxOccurrence([1,2,2,3,4,4,4,4,3,6,7,8,8,8,1,1,1,1,2,3,1,1,1]))
    pass
