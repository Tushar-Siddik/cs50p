def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in word:
        for vowel in vowels:
            if char.lower() == vowel:
                word = word.replace(char, '')
    return word

if __name__ == "__main__":
    main()

