#Advent of code Project 2
import re

#Open text file of lines
with open('day2.txt') as f:
    lines = f.readlines()

#Create dictionaries
allgames = {}
possiblecubes = {
    "blue": 14,
    "green": 13,
    "red": 12
}

#Set variable to hold possible index
possibleindex = 0

#Set variable to hold power of cube total
powerofcube = 0

#Loop through lines
for line in lines:
    #Do regex filter on line
    pattern = r'(\d+\s+\w+(?:,\s*\d+\s+\w+)*)'

    matches = re.findall(pattern, line)

    result = []
    for match in matches:
        group = match.split(', ')
        result.append(group)
    
    #Add result to dictionary
    allgames[(re.search("(?!Game )\d+(?=:)", line).group())] = result

#Loop through each game
for currentgame in allgames:
    gameispossible = True
    
    #Set dictionary to capture cubes found in this game
    foundcubes = {
    "blue": 0,
    "red": 0,
    "green": 0
    }
    
    #Set dictionary to capture larges number of each cube found in game
    leastnumberofcubes = {
    "blue": 0,
    "red": 0,
    "green": 0
    }
    #Loop through each pull
    for pull in allgames[currentgame]:

        #Loop through each cube in each pull
        for cube in pull:
            if "red" in cube:
                foundcubes["red"] = foundcubes["red"] + int(re.search("\d+", cube).group())
                #If number of cube is the largest so far, set it
                if int(re.search("\d+", cube).group()) > leastnumberofcubes["red"]:
                    leastnumberofcubes["red"] = int(re.search("\d+", cube).group())
            if "blue" in cube:
                foundcubes["blue"] = foundcubes["blue"] + int(re.search("\d+", cube).group())
                #If number of cube is the largest so far, set it
                if int(re.search("\d+", cube).group()) > leastnumberofcubes["blue"]:
                    leastnumberofcubes["blue"] = int(re.search("\d+", cube).group())
            if "green" in cube:
                foundcubes["green"] = foundcubes["green"] + int(re.search("\d+", cube).group())
                #If number of cube is the largest so far, set it
                if int(re.search("\d+", cube).group()) > leastnumberofcubes["green"]:
                    leastnumberofcubes["green"] = int(re.search("\d+", cube).group())

        #Check found cubes from this pull vs what is possible
        if foundcubes["red"] > possiblecubes["red"]:
            gameispossible = False
        elif foundcubes["blue"] > possiblecubes["blue"]:
            gameispossible = False
        elif foundcubes["green"] > possiblecubes["green"]:
            gameispossible = False
    
    
    #If game is still possible after all pulls then add index number of game
    if gameispossible == True:
        possibleindex = possibleindex + int(currentgame)
        print ("Game " + currentgame + " possible")
    else:
        print ("Game " + currentgame + " impossible")
    
    #Calculate power of least number cube
    powerofcube = powerofcube + (leastnumberofcubes["blue"] * leastnumberofcubes["red"] * leastnumberofcubes["green"])

#Print total index of possible games
print ("Index Total:" + str(possibleindex))

#Print total power of cubes
print ("Power Total:" + str(powerofcube))
