import random

COLORS = ["R", "G", "B", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

#function for genertaing the code

def generate_code():
    code = []

    for _ in range(CODE_LENGTH): # _ is a placeholder
        color = random.choice(COLORS) #what is .choice doing?
        code.append(color)

    return code

#function for player to guess code

def guess_code():
    while True: #invalid code will make it loop for another guess
        guess = input("Guess: ").upper().split(" ") #upper converts to enter input to uppercase

        if len(guess) != 4: 
             print(f"You must guess {CODE_LENGTH} colors.")
             continue #will being me to the top 
#Are the colors in the list?
        for color in guess: #looping through colors in uses guess
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again") #if colors not in list, it returns
                break #then breaks if to continue with the while loop if the colors are true
        else:
            break #breaking out of while loop, if the colors existed

    return guess #then return user guess

# Check Code - more complex

def check_code(guess, real_code): #does the guessing color match the real code color?
    color_count = {} # {} dictionary list
    correct_pos = 0 # check correct position
    incorrect_pos = 0 # check incorrect, do dont doublecount the color

    for color in real_code:
        if color not in color_count: 
            color_count[color] = 0 # If color is not a key in dictionary i want to add it
        color_count[color] += 1 #incrementing count in color dictionary

    for guess_color, real_color in zip(guess, real_code): # find colors in correct pos, zip takes 2 arguments and combine them into tuples
        if guess_color == real_color:
            correct_pos += 1
            color_count[guess_color] -= 1 #decrease color count from dictionary, makring color found is in correct pos

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_count and color_count[guess_color] > 0:
            incorrect_pos += 1 
            color_count[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to MasterMind, you have {TRIES} to guess code...")
    print("The valid colors are", *COLORS)

    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guess the code {attempts} tries!")
            break #breaks out of for loop

        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")

    else: #users did not guess right and did not break out of for loop
        print("You ran out of tries, the code was:", *code)

if __name__ == "__main__":
    game()