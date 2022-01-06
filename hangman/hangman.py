import random


def word_selected(fname):
    word_file = open('hangman.txt','r+')
    secret_word = random.choice(word_file.read().split())
    word_file.close()
    return secret_word

secret_word = word_selected('hangman.txt')
print(secret_word)

def word_selected_dashed():
    word_selected_dashed = []
    for i in range(len(secret_word)):
        word_selected_dashed.append('_')
    return ''.join(word_selected_dashed)

word_selected_dashed = word_selected_dashed()
print(word_selected_dashed)

trials = 7

gussed_word = list(word_selected_dashed)

while trials > 0:
    if ''.join(gussed_word) == secret_word:
        print("Congraluation, you have gussed the correct word")
        break

    print('you have got '+ str(trials)+ ' wrong tries ')
    user_guseed_letter = input('Guess a letter >>>>> \n')


    if user_guseed_letter in secret_word:
        print('Correct!')
        for i in range(len(secret_word)):
            if list(secret_word)[i] == user_guseed_letter:
                gussed_word[i] = user_guseed_letter
        print(''.join(gussed_word))

    elif user_guseed_letter not in secret_word:
        print('wrong!')
        trials -= 1

if trials == 0 :
    print('you have ran out of trials')