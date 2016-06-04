import re

def ques1():
    str = " AAAAA "
    str1 = " AAAAAAAA "
    str2 = " A "
    ary = [str,str1,str2]
    regex = r"^\sA{2,5}\s$"
    for item in ary:
        result = re.search(regex,item)        
        if result:
            print(result.group(0))
        else:
            print("None")
    pass


def ques2():
    str = "12.35 d sdf 45 r.4 -4.4 88.9";
    print("original str = {0}".format(str))
    print("regex str = {0}".format(re.sub(r"(-?\d+\.\d+)","float",str)))
    pass

def ques3():
    str = "12.35 d sdf 45 r.4 -4.4 88.9";
    print("original str = {0}".format(str))
    print("regex str = {0}".format(re.subn(r"(-?\d+\.\d+)","float",str)))
    pass

def ques4():
    regex = r"(?<!\S)[+-]?\d+(?!\S)"
    str = "12.35 d sdf 45 r.4 -4.4 88.9 54 34 -90";
    int_list = re.findall(regex,str)
    print(int_list)
    total = 0
    for x in int_list:
        total += int(x)
    average = total / len(int_list)
    print(average)
    pass

def ques5():
    regex = r"(?<=EE)\d{3}"
    replace = "461"
    str = "EE364 EE364"
    m = re.subn(regex,replace,str,count=1)
    print(m)
    pass

def ques6():
    regex = r"(?<!\S)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?!\S)"
    str = "192.168.1.1 200.117.05.03 a.bad.ip.adr 10.10.1 4.4.4.4.4.4 128.a.1.1"
    m = re.findall(regex,str)
    print(m)
    re.search
    pass

def ques7():
    #re.search("e",input, re.I) = search the pattern "e" in variable 'input' string, ignoring case sensitivity
    #re.match("(.*)(is a)(.*)", input) = match any substring of 'input' that has "is a" substring in it.
    #re.match("(?P<First>.*)(?P<Second>is a)(?P<Third>.*)",input) = has similar functionality as the previous string, with the first capturing group named 'First', second capturing group named 'Second' and third capturing group named 'Third'
    #re.search("(I){1}(like){10,}(you){1,2}",input) = search in 'input' string, for a substring with 'I' appearing for 1 time, 'like' appearing for at least 10 times, 'you' appearing only 1 or 2 times.
    
    pass

if __name__ == "__main__":
    
    pass
