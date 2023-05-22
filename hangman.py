#  still look for a txt file for word list so many words can be imported
import random
import string

# a word list or text file containing words can be used in place of the small word_lst i used to test

# the code commented below is just a sample txt file i used ..in same project directory
''' word_lst = []
with open('play_words.txt') as fl:
    for line in fl:
        word_lst.append(line.strip()) '''

# modify word_lst with your custom list or imported list or text file
word_lst = ['sleek', 'fisher', 'glare', 'ceder', 'monopoly']



#  rename this function to taste later on
def hangman():
    word = random.choice(word_lst).upper()
    word_letters = set(word)  # this is just to remove duplicates
    alphabets = set(string.ascii_uppercase)
    used_letters = set()  # see other method to declare an empty set {}* or so

    #  the .upper() method below doesn't throw any error since it has no effect on non-alpha characters

    print(' '.join(['_' for el in word]))
    attempt = 7
    while len(word_letters) > 0 and attempt > 0:
        print(f'you have {attempt} lives left')
        guess_letter = input('enter a letter to guess: ').upper()
        # this line below can work in place of the if condition used in the code...i.e using set properties
        # if guess_letter in alphabets and guess_letter not in used_letters
        if guess_letter in alphabets - used_letters:  # note sets can subtract from each other..to remove common element
            used_letters.add(guess_letter)
            attempt -= 1
            if guess_letter in word_letters:
                word_letters.remove(guess_letter)
                attempt += 1
                # this is to neutralise the lives/attempt deduction done above . i.e no live reduction for right attempt
                print('you guessed a matching letter correctly ')

        elif guess_letter in used_letters:
            print('you have already used this letter')

        else:
            print('pls enter a valid input, your input should be an alphabet')

        print('you have used the letters -->', '|'.join(used_letters))
        word_choice_list = [el if el in used_letters else '_' for el in word]
        print(' '.join(word_choice_list))

    if len(word_letters) == 0:
        print('nice job ... you got the word right')
    else:
        print('try better next time')
        print('the word is', word)

hangman()
# Todo: add a gui ..displaying the man hanging 