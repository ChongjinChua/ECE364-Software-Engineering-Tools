#! /usr/bin/env python3.4
import sys

def convert(list1):
    num_list = []
    str_list = []
    avg = []
    count = 0
    for x in list1.split():
        try:
            num_list.append(float(x))
            count += 1

        except ValueError:
            str_list.append(x)

    if num_list:
        sumval = 0
        for item in num_list:
            sumval += item

        avg.append(format(round((sumval/count),3),'.3f'))

    ret_tup = avg + str_list

    return tuple(ret_tup)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: parse.py [filename]")
        sys.exit(1)
        
    try:
        fp = open(sys.argv[1],'r')
    except IOError:
        print("{0} is not a readable file.".format(sys.argv[1]))
        sys.exit(1)

    for line in fp:
        output = convert(line)
        print(*output)


    fp.close()

    pass
