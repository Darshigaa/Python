import random

Health = 50

Difficulty = 3

Potion_Health = int(random.randint(25,50) / Difficulty)

Health = Health + Potion_Health

print(Health)

#random.randint generates a random number between two given integers. There is no random.randfloat. 'import' imports a moodule eg: random

#In 'Difficulty', number scheme is as follows: Easy = 1, Medium = 2, Hard = 3

#Casting - Changes one data typpe to another eg: From 'float' to 'int'



