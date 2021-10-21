from questions import quiz

def check_ans(question , ans , attempts , score):
    if quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer ! \n Your Score is {score+1}")
        return True
    else:
        print(f"Wrong Answer ! \n You have {attempts-1} left ! \n Try again .... ")
        return False

def print_dictionary():
    for question_id , question_answer in quiz.items():
        for key in question_answer:
            print(key + ":" , question_answer[key])
while True : 
    score = 0
    for question in quiz:
        attempts = 3
        while attempts > 0:
            print(quiz[question]["question"])
            answer = input("Enter Answer  (If you want to skip , please enter 'S') ")
            
            if  answer == "S":
                break
            check = check_ans(question,answer,attempts,score) 
            if check:
                score += 1
                break
            attempts -= 1
    break
print(f"Your Final score is {score}!\n\n")
print("The correct answer are .")
print_dictionary()
print("Thanks for playing . ")   
