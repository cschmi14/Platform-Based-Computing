def play(self):
    self.words = []
    self.guesses = []
    length = int(input("How long would you like your word to be? (enter a number)"))
    guessed_word = []
    for i in range(0, length):
        guessed_word.append('_')

    with open("dictionary.txt") as file:
        for line in file:
            line = line.strip()
            if len(line) == length:
                self.words.append(line)
    show_words = input("Would you like to see the remaining words after each guess? (yes/no)")
    if show_words == "yes":
        show_words = True
    else:
        show_words = False

    num_guesses = int(input("How many guesses would you like? (enter a number)"))
    guessed_letters = []
    while num_guesses >= 0 and len(self.words) > 1:
        guess = input("Please enter one character for your guess: ")
        while guess in guessed_letters:
            guess = input("You have already guessed that letter. Enter a new guess:")
        while not isinstance(guess, str) and not len(guess) == 1:
            guess = input("Invalid guess format. Enter a new guess that is one letter:")
        guessed_letters.append(guess)
        print()
        longest_count = 0
        longest_count_index = 0
        for i in range(0, length):
            curr_count = self.count_at_index(i, guess)
            if longest_count < curr_count:
                longest_count = curr_count
                longest_count_index = i

        if longest_count < self.count_without_guess(guess):
            words_new = []
            for word in self.words:
                if guess not in word:
                    words_new.append(word)
            self.words = words_new
            print("Incorrect Guess -", guess, "is not in the word!")
            num_guesses -= 1
            print("Number of guesses left:", num_guesses)
        else:
            words_new = []
            for word in self.words:
                if word[longest_count_index] == guess:
                    words_new.append(word)
            self.words = words_new
            print("Correct Guess -", guess, "is in the word!")
            print("Number of guesses left:", num_guesses)
            guessed_word[longest_count_index] = guess

        self.print_guessed_word(guessed_word)

        if show_words:
            print(self.words)

    correct_word = self.words[0]

    correct_guess = self.is_correct(guessed_word)

    while num_guesses >= 0 and not correct_guess:
        guess = input("Please enter one character for your guess: ")
        while guess in guessed_letters:
            guess = input("You have already guessed that letter. Enter a new guess:")
        guessed_letters.append(guess)
        if guess in correct_word:
            index_list = self.indices_of_guess(correct_word, guess)
            for i in index_list:
                guessed_word[i] = guess
        else:
            num_guesses -= 1
        correct_guess = self.is_correct(guessed_word)

    if not correct_guess:
        print("You lost! The word was:", self.words[0])
    else:
        print("You win! The word was:", self.words[0])


def count_at_index(self, index, guess):
    count = 0
    for word in self.words:
        if word[index] == guess:
            count += 1
    return count


def count_without_guess(self, guess):
    count = 0
    for word in self.words:
        if guess not in word:
            count += 1
    return count


def print_guessed_word(self, guessed_word):
    for i in range(0, len(guessed_word)):
        print(guessed_word[i], end=" ")
    print()


def indices_of_guess(self, correct_word, guess):
    index_list = []
    for i in range(0, len(correct_word)):
        if correct_word[i] == guess:
            index_list.append(i)
    return index_list


def is_correct(self, guessed_word):
    if "_" not in guessed_word:
        return True
    else:
        return False
