import random

def main():
    level = input_level("Level: ")
    level_range = random.randint(1, int(level))
    while True:
        guess = input_guess("Guess: ")

        if guess < level_range:
            print("Too small!")
        elif guess > level_range:
            print("Too large!")
        else:
            print("Just right!")
            break

def input_level(prompt):
    level = ""
    while not level.isnumeric():
        while level < "1":
            level = input(prompt)
    return int(level)

def input_guess(prompt):
    guess = ""
    while not guess.isnumeric():
        guess = input(prompt)
    return int(guess)

if __name__ == "__main__":
    main()

