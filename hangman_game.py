import hangman_constants as game_const
import random

# print(game_const.hangman_stages[0])
lives = 6
guessed = 0
index_of_body = 0
guessed_char_list = []
rand_letter= random.choice( game_const.words) #the letter to guess
len_rand_letter = len(rand_letter)
condition_satisfied = False

print(rand_letter)

while not condition_satisfied:

    user_could_guess = False

    for char in rand_letter:
        if char in guessed_char_list:
            print(char , end = "")
        else:
            print("_" , end= "")
    
    print("\n")

    # print(game_const.hangman_stages[index_of_body])
    user_guessed = input("Input a letter: ").lower()
    # print(f"user guessed: {user_guessed}")

    for char in rand_letter:
        if user_guessed == char and user_guessed not in guessed_char_list:
            guessed += 1
            user_could_guess = True

    if not user_could_guess:
        print("You could not guess...")
        lives -= 1
        index_of_body += 1
        print(game_const.hangman_stages[index_of_body])
        print(f"################ Lives left: {lives} #################")

    elif user_could_guess:
        print("You guessed...")
        guessed_char_list.append(user_guessed)
        print(game_const.hangman_stages[index_of_body])
        print(f"################ Lives left: {lives} #################")


    if ( (lives == 0) or (guessed == len_rand_letter) ) :
        condition_satisfied = True
        print("\t\tGAME OVER\t\t")

        if lives == 0:
            print("You lost hahahahaha")

        else:
            print("You won yayyyyyyy")