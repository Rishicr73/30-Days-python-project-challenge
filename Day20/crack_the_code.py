from random import sample

def get_code():
    c = ''.join([str(i) for i in range(10)])
    secret_number = ''.join(sample(c , k=3))
    return secret_number

def check_guessed_number(secret_number , guessed_number):
    correct_digits = len(set(secret_number) & set(guessed_number))
    correct_positions = sum([1 for m , n in zip(secret_number , guessed_number) if m == n ])
    return (correct_digits , correct_positions)

if __name__ == "__main__":
    life = 5
    secret_number = get_code()
    print("Get Ready to Crack the Code!\n")
    print("Computer will choose a three-digit random number,")
    print("which may start with zero and contains unique digits.")
    print(f"You have to guess it in {life} rounds.\n")
    while life :
        guessed_number = input("> ").strip()
        
        
        if not guessed_number.isnumeric():
            print("This is not a valid number .")
            continue

        if len(guessed_number) != 3:
            print("For your information, secret number is three-digits long.")
            continue

        correct_digits, correct_positions = check_guessed_number(secret_number, guessed_number)

        if correct_digits == 3 and correct_positions == 3:
            print("\nYay! You guessed it.\n")
            break

        print(f"You got {correct_digits} digit{'s' * (correct_digits > 1)} correct and {correct_positions} position{'s' * (correct_positions > 1)} correct.")
        life -= 1

    else:
        print("\nOhh no! Game Over.") 
        print(f"Secret number was {secret_number}.\n")   
