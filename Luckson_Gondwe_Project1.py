import random
import time

secret_word = ['bell', 'doll', 'golf', 'secret', 'thief']
word = random.choice(secret_word)
length = len(word)
name = input('what is your name: ')
print('welcome ' + name + ' Good luck!')
time.sleep(2)
print('Test begins now...')
time.sleep(2)

count = 0
display = '*' * length

def hangman(count, display, word):
    limit = 3
    guess = input('This is word: ' + display + ' Enter your guess: ')
    if guess in word:
        index = word.find(guess)
        word = word[:index] + '*' + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display)
    else:
        count += 1
        if count == 1:
            print('Incorrect. ' + str(limit - count) + ' guesses remaining')
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif count == 2:
            print('Incorrect. ' + str(limit - count) + ' guess remaining.')
            print("   _____ \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif count == 3:
            print('Incorrect. Game over :(')
            print("   ______ \n"
                  "  |      |\n"
                  "  |      | \n"
                  "  |      | \n"
                  "  |      O \n"
                 r"  |     /|\ " "\n"
                 r"  |     /|\ " "\n"
                  "__|__\n")
    if word == '*' * length:
        print('Congrats! You Got it!')
    elif count != limit:
        hangman(count, display, word)

hangman(count, display, word)


