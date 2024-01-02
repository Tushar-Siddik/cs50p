from datetime import date
import inflect
# pip install inflect
import sys

def main():
    user_input = input("Date of Birth: ")

    times = get_time(user_input)
    ntw = num_to_word(times)
    print(f"{ntw} minutes")


def get_time(user_input):
    today = date.today()

    try:
        dob = date.fromisoformat(user_input)
        times = today - dob
        return (times.days * 24 * 60)
    except ValueError:
        return sys.exit("Type in this format YYYY-MM-DD")


def num_to_word(num):
    p = inflect.engine()
    return p.number_to_words(num, andword="").capitalize()


if __name__ == "__main__":
    main()



# from datetime import date
# import inflect
# import sys
# import operator

# p = inflect.engine()


# def main():
#     try:
#         dob = input("Date of Birth: ")
#         # date.fromisoformat(dob) will check whether dob is a valid date or not
#         difference = operator.sub(date.today(), date.fromisoformat(dob))
#         print(convert(difference.days))
#     except ValueError:
#         sys.exit("Invalid date")


# def convert(time):
#     minutes = time * 24 * 60
#     return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"


# if __name__ == "__main__":
#     main()
