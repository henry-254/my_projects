import random

hangman_words = ["python", "javascript", "presented", "computergraphics", "system", "television"]
word = random.choice(hangman_words)
word_letters = set(word)
alphabet = set('abcdefghijklmnopqrstuvwxyz')
used_letters = set()

lives = 6

# function to print current state of the word
def print_word():
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print(' '.join(word_list))

# main game loop
while len(word_letters) > 0 and lives > 0:
    print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
    print_word()
    user_letter = input('Guess a letter: ').lower()
    if len(user_letter) == 1 and user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
        else:
            lives -= 1
            print('Letter is not in the word.')
    elif user_letter in used_letters:
        print('You have already used that letter. Please try again.')
    else:
        print('Invalid input. Please try again.')
    
# end game loop
if lives == 0:
    print('You died, sorry. The word was', word)
else:
    print('Congratulations! You guessed the word', word, '!!')
