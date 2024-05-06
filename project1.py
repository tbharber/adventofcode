#Advent of code Project 1

#Open text file of lines
with open('project1.txt') as f:
    lines = f.readlines()

#Create list to hold all numbers
totalnumlist = []

#Loop through lines
for line in lines:
    #Loop through characters in line
    for char in line:

        #If character is a number
        if char.isdigit():
            #Get number
            firstnum = char
            break

    #Loop through characters in line
    for char in reversed(line):
        #If character is a number
        if char.isdigit():
            #Get number
            secondnum = char
            break
    
    #Add current list of digits to total list
    totalnumlist.append(firstnum + secondnum)

#Loop through list 
for currentnum in totalnumlist:
        #Add numbers in list together
        totalvalue = totalvalue + int(currentnum)


print (totalvalue)
    