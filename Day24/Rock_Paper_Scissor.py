#Rock , Paper , Scissor .  
import random
print('WELCOME!')
char = 'RPS'
def winner(computer , player):
    if computer == player:
        print("It's a Tie !")
    elif computer == 'R'  and player  == 'P'  :
        print("You won")
    elif computer == 'R'  and player == 'S':
        print('Computer won')
    elif computer == 'S'  and  player == 'R':
        print('You won')
    elif computer == 'P'  and player == 'R' :
        print('computer won') 
    elif computer == 'S' and player == 'P':
        print('Computer won')
    elif computer == 'P' and player  == 'S' :
        print('You won')
    else:
        print("Please choose Between R(ROCK),P(PAPER),S(SCISSOR)")  
while True:
    player = input('R = Rock , P = Paper , S = Scissor : \n').upper()
    computer = random.choice(char)      
    print(winner(computer , player))
    s = input('Do you want to play again ? yes or No \n').lower()
    if s == 'no':
        break 
