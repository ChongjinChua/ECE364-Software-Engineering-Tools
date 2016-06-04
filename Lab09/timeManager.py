#! /usr/bin/env python3.4
import re, timeDuration

def getTotalEventSpan(eventName):
    weeks = 0
    days = 0
    hours = 0
    with open("Events.txt") as fptr:
        all_lines = fptr.readlines()

    for line in all_lines[2:]:
        line = line.split()
        name = line[0].strip()
        if eventName == name:
            duration = line[1].strip()
            iterations = line[2].strip()
            print(iterations)
            if duration[2] == 'w':
                weeks += int(duration[0:2]) * int(iterations)
            if duration[2] == 'd':
                days += int(duration[0:2]) * int(iterations)
            if duration[2] == 'h':
                hours += int(duration[0:2]) * int(iterations)

    return timeDuration.TimeSpan(weeks,days,hours)

def rankEventsBySpan(*args):
    lst = []
    for item in args:
        time = getTotalEventSpan(item)
        lst.append(time.getTotalHours())
    lst.sort()
    lst_rtn = []
    for time in lst:
        for item in args:
            total = getTotalEventSpan(item)
            if(time == total.getTotalHours()):
                lst_rtn.append(item)

    lst_final = []
    for item in range(1,len(lst_rtn)+1):
        lst_final.append(lst_rtn[-item])
        
    return lst_final
        


if __name__ == "__main__":
    getTotalEventSpan("hello")
    pass
