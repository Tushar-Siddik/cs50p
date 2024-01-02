def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return starts_with_letters(s) and valid_length(s) and no_middle_numbers(s) and no_punctuation(s)

def starts_with_letters(s):
    return s[:2].isalpha()

def valid_length(s):
    return 2 <= len(s) <= 6

def no_middle_numbers(s):
    char_list = []
    num_list = []
    for char in s:
        if char.isalpha():
            char_list.append(char)
        else:
            num_list.append(char)

    char_index = s[: : -1].index(char_list[-1])
    if len(num_list) >= 1:
        if num_list[0] == '0':
            return False
        else:
            if s[3].isnumeric() and len(s) > 4:
                return s[4].isnumeric()
            else:
                num_index = s[: : -1].index(num_list[-1])
                return char_index > num_index
    return True


def no_punctuation(s):
    return all(char.isalnum() for char in s)

if __name__ == "__main__":
    main()
