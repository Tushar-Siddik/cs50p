import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        problem = f"{x} + {y} = "
        correct_answer = x + y
        tries = 0

        while tries < 3:
            user_answer = input(problem)
            try:
                user_answer = int(user_answer)
                if user_answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1

        if tries == 3:
            print(f"{problem}{correct_answer}")

    print(f"Score: {score}")

def get_level():
    level_list = ['1', '2', '3']
    level = ''
    while level not in level_list:
        level = input("Level: ")
    return int(level)

def generate_integer(level):
    max_value = 10 ** level - 1
    if level == 1:
        return random.randint(0, max_value)
    elif level == 2:
        return random.randint(10, max_value)
    return random.randint(100, max_value)

if __name__ == "__main__":
    main()
