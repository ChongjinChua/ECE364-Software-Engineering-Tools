#! /usr/bin/env python3.4

from pprint import pprint as pp
import re

class Simulation:

    def __init__(self,simnNo,simDate,chipName,chipCount,chipCost):
        self.simulationNumber = simnNo
        self.simulationDate = simDate
        self.chipName = chipName
        self.chipCount = chipCount
        self.chipCost = chipCost
        self.simulationCost = chipCost * chipCount
        pass
        
    def __str__(self):
        rtn_str = str(self.chipName) + ": " + str("%03d" %self.simulationNumber) + ", " + self.simulationDate + ", $" + str("%06.2f" %self.simulationCost)
        return rtn_str
        
class Employee:

    def __init__(self,employeeName,employeeID):
        self.employeeName = employeeName
        self.employeeID = employeeID
        self.simulationsDict = {}
        self.simulationFreq = 0

    def addSimulation(self,sim):
        exist = self.simulationsDict.get(sim.simulationNumber,"missing")
        if exist == "missing":
            self.simulationsDict[sim.simulationNumber] = sim
        else:
            self.simulationsDict.update({sim.simulationNumber:sim})
        self.simulationFreq += 1
            
    def getSimulation(self,simNo):
        exist = self.simulationsDict.get(simNo,None)
        return exist

    def __str__(self):
        rtn_str = self.employeeID+", "+self.employeeName+": "+str("%02d" %self.simulationFreq)+" "+"Simulations"
        return rtn_str

    def getWorkload(self):
        header = self.__str__()
        sim_list = []
        sim_str = ""

        for value in self.simulationsDict.values():
            sim_list.append(value.__str__())

        sim_list.sort()
        for si in sim_list:
            sim_str += si
            sim_str += "\n"
            
        rtn_str = header + "\n" + sim_str.rstrip()
        print(rtn_str)
        return rtn_str

    def addWorkload(self,fileName):

        with open(fileName,'r') as fptr:
            all_lines = fptr.readlines()
        #print(all_lines[2].split())
        for line in all_lines[2:]:
            line = line.split()
            #print(line)
            nmemb = Simulation(int(line[0]),line[1],line[2],int(line[3]),float(line[4].lstrip('$')))
            self.addSimulation(nmemb)

class Facility:
    def __init__(self, facilityName):
        self.facilityName = facilityName
        self.employeesDict = {}
        self.employeesNum = 0

    def addEmployee(self, employee):
        self.employeesDict.update({employee.employeeName:employee})
        self.employeesNum += 1

    def getEmployees(self, *args):
        rtn_list = []
        if len(args) == 1:
            rtn_list.append(self.employeesDict[args[0]])
        else:
            for name in args:
                rtn_list.append(self.employeesDict[name])
        return rtn_list

    def __str__(self):
        header = self.facilityName +": "+str("%02d" %self.employeesNum)+" "+"Employees"
        sim_list = []
        sim_str = ""

        for value in self.employeesDict.values():
            sim_list.append(value.__str__())

        sim_list.sort()
        for si in sim_list:
            sim_str += si
            sim_str += "\n"

        rtn_str = header + "\n" + sim_str.rstrip()
        #print(rtn_str)
        return rtn_str

    def getSimulation(self,simNo):
        for emp in self.employeesDict.values():
            for sim in emp.simulationsDict.values():
                if str(simNo) in str(sim):
                    return sim

if __name__ == "__main__":


    pass
