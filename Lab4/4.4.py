# Define a list of survey response values and store them ub a variable.
# Next define a tuple of response IDs.
# Name: Keane Kouchi
# Date: 9/18/24

SurveyResponses = [5, 7, 3, 8]

#SurveyResponses.append(0)

#examples
#SurveyResponses.insert(2,6)
#SurveyResponses.sort()
#SurveyResponses.remove()

#SurveyResponses = SurveyResponses + [0]
SurveyResponses = SurveyResponses[0:2] + [6] + SurveyResponses[2:] + [0]

print(SurveyResponses)