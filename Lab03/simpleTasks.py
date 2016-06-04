#$Author: ee364g13 $
#$Date: 2016-02-03 14:58:03 -0500 (Wed, 03 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364g13/Lab03/simpleTasks.py $
#$Revision: 87655 $
#$Id: simpleTasks.py 87655 2016-02-03 19:58:03Z ee364g13 $

def getPairwiseDifference(vec):
    if type(vec) is not list:
        return None
    elif len(vec) == 0:
        return None
    else:
        mylist = []
        vec_range = range(len(vec))[1:]
        for index in vec_range:
            mylist.append(vec[index]-vec[index-1])
        return mylist

def flatten(l):
    if type(l) is not list:
        return None
    for item in l:
        if type(item) is not list:
            return None
    mylist = []
    for item in l:
        mylist += item
    return mylist

def partition(l,n):
    if type(l) is not list:
        return None
    elif len(l) == 0:
        return None
    else:
        mylist = []
        mylist_index = 0
        while (len(l)-mylist_index > n):
            mylist.append(l[mylist_index:mylist_index+n])
            mylist_index += n
        mylist.append(l[mylist_index:])
        return mylist

def rectifySignal(signal):
    if type(signal) is not list:
        return None
    elif len(signal) == 0:
        return None
    else:
        for index in range(len(signal)):
            if(signal[index] < 0):
                signal[index] = 0
        return signal

def floatRange(a,b,s):
    if a >= b:
        return None
    else:
        my_range = int((b - a)/s)
        mylist = []
        for index in range(my_range):
            mylist.append(round(float(a),1))
            a = round(a + s,1)
        mylist.append(a)
        return mylist

def getLongestWord(sentence):
    if type(sentence) is not str:
        return None
    sentence_list = sentence.split()
    if len(sentence_list) < 2:
        return None
        
    longest_word = sentence_list[0]
    highest_count = len(longest_word)
    
    for item in sentence_list[1:]:
        if len(item) > highest_count:
            highest_count = len(item)
            longest_word = item
    return longest_word

def decodeNumbers(l):
    if type(l) is not list:
        return None
    for item in l:
        if type(item) is not int:
            return None
    mystring = ""
    for item in l:
        mystring += chr(item)
    return mystring

def getCreditCard(s):
    if not s:
        return None
    mylist = []
    for item in s:
        if item.isdigit():
            mylist.append(int(item))
    return mylist

if __name__ == "__main__":
    #print(getPairwiseDifference([8,4,15,10,12,14,13]))
    #print(getPairwiseDifference(4))
    #print(getPairwiseDifference([]))
   # print(flatten([[2,3,1],[9],[7,-1]]))
   # print(flatten([[2,3,1],[9,2],[7,-1]]))
    #print(partition([11,18,15,21,19,13,14,17],3))
    #print(partition([15,23,28,19,22,29],2))
    #print(rectifySignal([1.0,0.81,-28,-0.19,0,0.1]))
    #print(floatRange(0,4,0.5))
    #print(floatRange(1,3,0.2))
    #print(floatRange(4,5,0.1))
    #print(getLongestWord("the weather is cool today"))
    #print(getLongestWord("Scooby is cute"))
    #print(decodeNumbers([72, 101, 108, 108, 111, 33]))
    #print(getCreditCard("")
    #print(getCreditCard("Sherlock Holmes 1234-5678-7845-2050"))
    #print(getCreditCard("Sherlock 1234567878452050"))
    #print(getCreditCard("Sherlock yo Holmes 1234 5678 7845 2050"))
    pass
