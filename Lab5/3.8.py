# Create a dictionary with ID values as the keys and survey responses as the 
# values using zip()
# Name: Keane Kouchi
# Date: 9/20/24


SurveyResponses = [5, 7, 3, 8]
ResponseIDs = (1012, 1035, 1021, 1053)

ResponsesAndIDsDict = dict(zip(ResponseIDs, SurveyResponses))

print("The survey data is:", ResponsesAndIDsDict)
