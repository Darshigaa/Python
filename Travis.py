known_users = ["Alexander", "Antonio", "Bob", "Claire", "Cole", "Daphne", "Dylan", "Emelia", "Francis", "Gusty"]

while True:
    print("Hi! I am Travis!")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!You are now authorized!".format(name))
        remove = input("Would you like to be removed from the system? (Yes/No): ").lower().strip()
        if remove == "yes":
            known_users.remove(name)
        elif remove == "no":
            print("No problem! I don't ever want you to leave!")
            
    else:
        print("I don't think I know you {}!".format(name))
        add_me = input("Would you like to be added to the system? (Yes/No) :").lower().strip()
        if add_me == "yes":
            known_users.append(name)
        elif add_me == "no":
            print("No problem! I would've loved for you to join, but i guess we won't be friends now.:(")
        
   
        
        
     
    
    
