import random
words = ["whatever", "waifu", "anime", "why", "shrek","guess", "endgame", "quintessential","rhetoric", "infinitesimal"]
secret_word = random.choice(words)
dashes = ""
for i in range(len(secret_word)):
    dashes+= "-"
def get_guess():
    letter = input("Guess: ")
    while True:
        while len(letter) != 1:
            print ("Your guess must have exactly one character!")
            letter = input("Guess: ")
        while not letter.islower():
            print ("Your guess must be a lowercase letter!")
            letter = input("Guess: ")
        if len(letter) != 1 or not letter.islower():
            continue
        return letter
def update_dashes(word, dash_count, le_guess):
    i = 0
    dash_count = list(dash_count)
    for letter in word:
        if le_guess == letter:
            dash_count[i] = letter
        i+= 1
    dash_count = "".join(dash_count)
    return dash_count
guesses_left = 10
while True:
    print (dashes)
    print (str(guesses_left) + " incorrect guesses left.")
    the_guess = get_guess()
    in_there = False
    for letter in secret_word:
        if letter == the_guess:
            print ("That letter is in the secret word")
            in_there = True
            break
    if not in_there:
        print ("Not in there")
        guesses_left -= 1
    dashes = update_dashes(secret_word, dashes, the_guess)
    if dashes == secret_word or guesses_left ==0:
        stay = False
    else:
        stay = True
    if not stay:
        break
if dashes == secret_word:
    print ("You did it!")
    print ("The secret word is:" + secret_word)
else:
    print ("You lose! The word was " + secret_word)
