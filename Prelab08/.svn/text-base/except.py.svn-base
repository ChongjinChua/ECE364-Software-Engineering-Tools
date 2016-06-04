#! /usr/bin/env python3.4

def convert(list1):
    new_list = []
    for x in list1.split():
        try:
            new_list.append(float(x))
        except ValueError:
            pass
            #raise ValueError("can't convert string")

    sumval = 0
    for item in new_list:
        sumval += item

    return sumval

if __name__ == "__main__":
    list1 = input("Please enter some values: ")
    print("The sum is: {0}".format(convert(list1)))
    pass
