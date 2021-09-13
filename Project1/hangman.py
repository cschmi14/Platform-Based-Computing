class Hangman:
  		  	   		     			  		 			 	 	 		 		 	 		 		 	 		  	 	 			  	 
    def __init__(self, words=[], guesses=[]):
        self.words = words
        self.guesses = guesses

    def __str__(self):
        return self.guesses

    def play(self):
        self.words = []
        self.guesses = []
        length = get_length()
        guessed_word = init_guessed_word(length)
        init_words_list(self, length)

        show_words = input("Would you like to see the remaining words after each guess? (yes/no)")
        if show_words == "yes":
            show_words = True
        else:
            show_words = False

        num_guesses = get_num_guesses()
        guessed_letters = []
        while num_guesses > 0 and length > 1:
            guess = get_guess(guessed_letters)
            guessed_letters.append(guess)

            self.words = longest_word_family(self, guess)

            if guess in self.words[0]:
                guessed_word = correct_guess_message(self, guess, length, guessed_word)
            else:
                guessed_word = incorrect_guess_message(guess, guessed_word)
                num_guesses -= 1
            if game_win(self, guessed_word):
                return
            print("Number of guesses left :", num_guesses)
            print("Previously Guessed Letters:", guessed_letters)
            print_current_guesses(guessed_word)
            print_remaining_words(self, show_words)

        print("You ran out of guesses! The word was :", self.words[0])


def get_guess(guessed_letters):
    guess = input("Please enter one character for your guess: ")
    while guess in guessed_letters or not guess.isalpha() or len(guess) > 1 or len(guess) < 1:
        if guess in guessed_letters:
            guess = input("You have already guessed that letter. Enter a new guess:")
        else:
            guess = input("Invalid guess format. Enter a new guess that is one letter:")
    print()
    return guess


def get_num_guesses():
    num_guesses = input("How many guesses would you like? (enter a number)")
    while True:
        try:
            num_guesses = int(num_guesses)
            return int(num_guesses)
        except ValueError:
            num_guesses = input("Number entered was not an integer. Please enter a number for the number of guesses:")


def get_length():
    length = input("How long would you like your word to be? (enter a number)")
    while True:
        try:
            length = int(length)
            while int(length) >= 30:
                length = input("Length must be less than 30. Please enter a new number for the word length:")
                length = int(length)
            return int(length)
        except ValueError:
            length = input("Length entered was not an integer. Please enter a number for the word length:")


def longest_word_family(self, guess):
    word_families = dict()
    family = ""
    without_guess_family = ""
    for word in self.words:
        for letter in word:
            if letter == guess:
                family += letter
            else:
                family += '-'
        if family not in word_families:
            word_families[family] = []
            word_families[family].append(word)
        else:
            word_families[family].append(word)
        family = ""
    for i in range(0, len(self.words[0])):
        without_guess_family += '-'
    # for family in word_families:
    #     print(word_families[family])
    return find_largest_word_family(word_families, without_guess_family)


def find_largest_word_family(word_families, without_guess_family):
    max_length = 0
    max_length_family = ""
    for family in word_families:
        if max_length < len(word_families[family]):
            max_length = len(word_families[family])
            max_length_family = family
    # if there is a tie between a family with guess in it and a family without, we choose the family without guess
    # to make the game even harder to win
    if without_guess_family in word_families and max_length == len(word_families[without_guess_family]):
        return word_families[without_guess_family]
    return word_families[max_length_family]


def init_guessed_word(length):
    guessed_word = []
    for i in range(0, length):
        guessed_word.append('_')
    return guessed_word


def init_words_list(self, length):
    max_length = 0
    with open("dictionary.txt") as file:
        for line in file:
            line = line.strip()
            if len(line) == length:
                self.words.append(line)


def correct_guess_message(self, guess, length, guessed_word):
    for i in range(0, length):
        if self.words[0][i] == guess:
            guessed_word[i] = guess
    print("Correct Guess! :", guess, "is in the word")
    return guessed_word


def incorrect_guess_message(guess, guessed_word):
    print("Incorrect Guess :", guess, "is not in the word")
    return guessed_word


def print_current_guesses(guessed_word):
    print()
    for letter in guessed_word:
        print(letter, end=" ")
    print()
    print()


def print_remaining_words(self, show_words):
    if show_words:
        print(self.words)


def game_win(self, guessed_word):
    if len(self.words) == 1 and ''.join(guessed_word) == self.words[0]:
        print("Congratulations, you guessed the word! The word was:", self.words[0])
        print()
        return True
    else:
        return False

