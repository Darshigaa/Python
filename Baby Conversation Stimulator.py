from random import choice

questions = ["Why is the sky blue?", "Why do we have a remote for the tv?", "Why do we need to go to school?"]

question = choice(questions)
answer = input(question)

while answer!="Just because!":
   answer = input("But why?: ")

print ("Oh!... Okay...")


       
    
    

