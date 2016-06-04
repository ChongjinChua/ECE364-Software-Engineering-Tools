#! /usr/bin/env python3.4
import re

class TimeSpan:
    def __init__(self, weeks, days, hours):
        if type(weeks) is not int or type(days) is not int or type(hours) is not int:
            raise TypeError("Only integers")
        elif weeks < 0 or days < 0 or hours < 0:
            raise ValueError("must be non-negative")
        
        self.hours = hours%24
        self.days = int(hours/24) + days
        self.weeks = int(self.days/7) + weeks
        self.days %= 7

    def __str__(self):
        self.weekstr = str(self.weeks)
        self.daystr = str(self.days)
        self.hourstr = str(self.hours)
        if self.weeks < 10:
            self.weekstr = '0' + self.weekstr
        if self.hours < 10:
            self.hourstr = '0' + self.hourstr
        return self.weekstr + 'W ' + self.daystr + 'D ' + self.hourstr + 'H'

    def getTotalHours(self):
        total = self.weeks * (7 * 24) + self.days * 24 + self.hours
        return total

    def __add__(self, other):
        if type(other) is not TimeSpan:
            raise TypeError("must be of TimeSpan type")
        return TimeSpan(self.weeks+other.weeks,self.days+other.days,self.hours+other.hours)

    def __mul__(self, other):
        if type(other) is not int or type(self) is not TimeSpan:
            raise TypeError("INT is expected")
        elif other <= 0:
            raise ValueError("must be non-negative")

        return TimeSpan(self.weeks*other,self.days*other,self.hours*other)

    def __rmul__(self,other):
        if type(other) is not int or type(self) is not TimeSpan:
            raise TypeError("INT is expected")
        elif other <= 0:
            raise ValueError("must be non-negative")

        return TimeSpan(self.weeks*other,self.days*other,self.hours*other)
        

if __name__ == "__main__":
    pass
