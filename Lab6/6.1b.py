# Create a conditional expression that prints true if the last element of
# a tuple is "Happy" and it contains more than 3 elements
# Name: Keane Kouchi
# Date: 9/25/24

Emotions = ("Happy", "Sad", "Fear", "Surprise")

# To test True results
#Emotions = ("Surprise", "Sad", "Fear", "Happy")

#To test False results
#Emotions = ("Sad", "Fear", "Happy")

Result = "True" if (Emotions[-1] == "Happy" and len(Emotions) > 3) else "False"

print("The last element of the tuple is Happy and there are more than 3 values:",Result)