#!/bin/bash/env python3

import csv
import sys



def sysmon_Parse(file_path):
    output = []
    with open(file_path) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            inner_list = []
            list_Column5 = row[5].split('\n')
            #The two items in the if statement can be changed to any str search 
            if 'WINWORD.EXE' in row[5] and 'msdt.exe' in row[5]:
                path = list_Column5[11].split('CommandLine: ')
                inner_list.append(row[1])
                inner_list.append(path[1])
                output.append(inner_list)
    return output

