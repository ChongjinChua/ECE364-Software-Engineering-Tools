#! /usr/bin/env python3.4

from math import floor


def find_median(list1,list2):
    comb_list = list1 + list2
    comb_list.sort()
    comb_len = len(comb_list)
    if (comb_len-1) % 2 != 0:
        median = comb_list[floor((comb_len - 1) / 2)]
    else:
        median = comb_list[int((comb_len - 1) / 2)]

    return tuple([median,comb_list])