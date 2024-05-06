#Advent of code Project 1
import time

#Open text file of lines
with open('project1.txt') as f:
    lines = f.readlines()

#Create list to hold all numbers
totalnumlist = []

#Loop through lines
for line in lines:
    #Find index's of all digits and number strings

    num1 = line.find('1')
    num2 = line.find('2')
    num3 = line.find('3')
    num4 = line.find('4')
    num5 = line.find('5')
    num6 = line.find('6')
    num7 = line.find('7')
    num8 = line.find('8')
    num9 = line.find('9')

    str1 = line.find('one')
    str2 = line.find('two')
    str3 = line.find('three')
    str4 = line.find('four')
    str5 = line.find('five')
    str6 = line.find('six')
    str7 = line.find('seven')
    str8 = line.find('eight')
    str9 = line.find('nine')

    print (num1, num2, num3, num4, num5, num6, num7, num8, num9, str1, str2, str3, str4, str5, str6, str7, str8, str9)
    time.sleep(40)

    
    #Add current list of digits to total list
    #totalnumlist.append(firstnum + secondnum)

#Loop through list 
#for currentnum in totalnumlist:
        #Add numbers in list together
        #totalvalue = totalvalue + int(currentnum)


#print (totalvalue)
    