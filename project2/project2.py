#Advent of code Project 2
import re

#Open text file of lines
with open('project2.txt') as f:
    lines = f.readlines()

#Create dictionary
games = {}

#Loop through lines
for line in lines:
    games[(re.search("(?!Game )\d+(?=:)", line).group())] = {}
print (games)
