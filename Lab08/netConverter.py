#! /usr/bin/env python3.4
import re, math, HardwareTasks

def verilog2vhdl(ver_line):

    #print(vnl)
    try:
        vnl = HardwareTasks.processLine(ver_line)
        port_pin = vnl[2]
        port_len = len(port_pin)
        i = 1
        rtn_str = vnl[1] + ": " + vnl[0] + " PORT MAP("
        for item in port_pin:
            if i < port_len:
                rtn_str += item[0] + "=>" + item[1] + ', '
            else:
                rtn_str += item[0] + "=>" + item[1] + ");"
            i += 1

        return rtn_str

    except ValueError:

        return "Error: Bad Line."
        

def convertNetlist(sourceFile, targetFile):
    fpr = open(sourceFile,'r')
    fpw = open(targetFile,'w')
    write_list = []
    all_lines = fpr.readlines()
    for line in all_lines:
        write_list.append(verilog2vhdl(line))

    final = '\n'.join(write_list)
    
    fpw.write(final)
    
    fpr.close()
    fpw.close()

if __name__ == "__main__":
    pass
