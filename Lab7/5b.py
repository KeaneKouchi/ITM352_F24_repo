# Develop a program using (1980, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989) 
# and (17, 35, 26, 26, 25, 27, 35, 21, 19), which appends the values to two lists. 
# Then store the lists as values in a dictionary with keys “years” and “respondents.”
# without using loops
# Keane Kouchi
# 9/27/2024


Years = (1980, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989)
Respondents = (17, 35, 26, 26, 25, 27, 35, 21, 19)

MyDict = dict(zip(Years, Respondents))

print(MyDict)