movies = {
    "Finding Dory":{"Rating":3,"Availability":4},
    "Bourne":{"Rating":18,"Availability":6},
    "Tarzan":{"Rating":15,"Availability":9},
    "Ghost-Busters":{"Rating":9,"Availability":2}
    }
while True:
    choice = input("What movie would you like to watch?: ").strip().title()

    if choice in movies:
        age = int(input("How old are you?: ").strip())

        if age >= movies[choice]["Rating"]:
            #check user age
            if movies[choice]["Availability"] > 0:
                print("Enjoy the film!")
                movies[choice]["Availability"] = movies[choice]["Availability"] - 1
            else:
                print("Sorry!Seats are not available!")
            
        else:
            print("You are to young to watch that film!Sorry!")
        
    else:
        print("Sorry! We don't have that film!")
        
    
