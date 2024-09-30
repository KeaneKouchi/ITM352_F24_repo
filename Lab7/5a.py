# Develop a program that will iterate through the tuples (1980, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989) 
# and (17, 35, 26, 26, 25, 27, 35, 21, 19), which correspond to survey years and respondents in those years 
# and append the values to two lists. Then store the lists as values in a dictionary with keys “years” and “respondents.”
# Keane Kouchi
# 9/27/2024

Years = (1980, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989)
Respondents = (17, 35, 26, 26, 25, 27, 35, 21, 19)

ListLen = len(Years)
MyDict = {}
index = 0

#while index < ListLen:
#    MyDict[Years[index]] = Respondents[index]
#    index += 1

for index in range(len(Years)):
    MyDict[Years[index]] = Respondents[index]

print(MyDict)