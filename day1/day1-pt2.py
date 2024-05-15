#Advent of code Project 1, part 2
import re

#Open text file of lines
with open('day1.txt') as f:
    lines = f.readlines()

#Create integer to hold total
totalvalue = 0

#Loop through lines
for line in lines:
    #Create empty list for current line
    currentlinenumber = []
    currentlineindex = []

    # This secion finds the index number of each occurence of digits 1-9 and words one-nine and adds each occurence to the current list
    # Created in format of [ [6,0], [7,7], [4,22], [7,23] ]
    # For each sub list, first digit is the found number and second digit is the index
    for m in re.finditer('1', line):
        currentlinenumber.append(1)
        currentlineindex.append(m.start())
    for m in re.finditer('2', line):
        currentlinenumber.append(2)
        currentlineindex.append(m.start())
    for m in re.finditer('3', line):
        currentlinenumber.append(3)
        currentlineindex.append(m.start())
    for m in re.finditer('4', line):
        currentlinenumber.append(4)
        currentlineindex.append(m.start())
    for m in re.finditer('5', line):
        currentlinenumber.append(5)
        currentlineindex.append(m.start())
    for m in re.finditer('6', line):
        currentlinenumber.append(6)
        currentlineindex.append(m.start())
    for m in re.finditer('7', line):
        currentlinenumber.append(7)
        currentlineindex.append(m.start())
    for m in re.finditer('8', line):
        currentlinenumber.append(8)
        currentlineindex.append(m.start())
    for m in re.finditer('9', line):
        currentlinenumber.append(9)
        currentlineindex.append(m.start())
    for m in re.finditer('one', line):
        currentlinenumber.append(1)
        currentlineindex.append(m.start())
    for m in re.finditer('two', line):
        currentlinenumber.append(2)
        currentlineindex.append(m.start())
    for m in re.finditer('three', line):
        currentlinenumber.append(3)
        currentlineindex.append(m.start())
    for m in re.finditer('four', line):
        currentlinenumber.append(4)
        currentlineindex.append(m.start())
    for m in re.finditer('five', line):
        currentlinenumber.append(5)
        currentlineindex.append(m.start())
    for m in re.finditer('six', line):
        currentlinenumber.append(6)
        currentlineindex.append(m.start())
    for m in re.finditer('seven', line):
        currentlinenumber.append(7)
        currentlineindex.append(m.start())
    for m in re.finditer('eight', line):
        currentlinenumber.append(8)
        currentlineindex.append(m.start())
    for m in re.finditer('nine', line):
        currentlinenumber.append(9)
        currentlineindex.append(m.start())

    #Get smallest number
    smallestindexeddigit = currentlinenumber[currentlineindex.index(min(currentlineindex))]

    #Get largest number
    largestindexeddigit = currentlinenumber[currentlineindex.index(max(currentlineindex))]

    #Add both numbers to total
    totalvalue = totalvalue + int(str(smallestindexeddigit) + str(largestindexeddigit))

#Print final total
print (totalvalue)