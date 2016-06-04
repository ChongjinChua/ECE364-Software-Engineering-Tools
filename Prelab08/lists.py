#! /usr/bin/env python3.4
from listmod import find_median


if __name__ == "__main__":
    list1 = input("Enter the first list of numbers: ")
    list2 = input("Enter the second list of numbers: ")

    list1 = [int(x) for x in list1.split()]
    list2 = [int(x) for x in list2.split()]

    print("First list: {0}".format(list1))
    print("Second list: {0}".format(list2))

    (Median, Sorted_List) = find_median(list1,list2)

    print("Merged list: {0}".format(Sorted_List))
    print("Median: {0}".format(Median))

    pass
