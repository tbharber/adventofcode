#Advent of code Project 2
import re
import time

#Open text file of lines
with open('project2.txt') as f:
    lines = f.readlines()

#Create dictionary
games = {}

#Loop through lines
for line in lines:
    #Get game # and add to dictionary
    games[(re.search("(?!Game )\d+(?=:)", line).group())] = (re.search("(?<=(;|:) )(.*?)(?=(;|$))", line).group())
    
    #Set regex pattern to find number of marbles
    pattern = r'\b(?:\d+\s+\w+(?:,\s+\d+\s+\w+)*)(?=\s*;|\s*$)'

    #Do regex and add to dictionary
    games[(re.search("(?!Game )\d+(?=:)", line).group())] = re.findall(pattern, line)

#Loop through each dictionary
for x in games:

    print (games[x])
