#Basic beginner game in python

print("Welcome to the Game!")
name = input("What is your Name? ")
age = int(input("what is your age? "))



Health = 10



if age >= 18:
    print("Great , Get Ready!")
    print("You are starting with",Health,"health")

    wants_play = input("Do you want to play? ").lower()
    if wants_play == "yes":
        print("let's play!")

        left_or_right = input("First choice..left 0r right(left/Right)?").upper()
        if left_or_right == "LEFT":
            ans = input("Nice,you follow the path and reach a lake...Do you swim across or go around(across/around)?").lower()
            if ans == "around":
                print("You went around and reached the other side of lake")
            elif ans == "across"    :
                print("you managed to get across,but were bit by a fish and lost 5 health")
                print("Now you have only 5 health remaining")
                Health -= 5

            ans = input("You notice a house and a river ,which  do you go to (river/house)").upper()  
            if ans == "HOUSE":
                print("You got to the house and are greted by the owner...He doesn't like you and you lost 5 health")
                Health -= 5
                
                if Health <= 0:
                    print("You have 0 health so you lost")
                else:
                    print("You win,congrats!")    

            else :
                print("oops you fall in a river")

        else :
            print("You fell down and lost...")    
   
else :
    print("You are not Enough to play")  
    
