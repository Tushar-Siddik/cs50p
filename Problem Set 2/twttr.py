vowels = ['a', 'e', 'i', 'o', 'u']
text = input("Input: ")

for character in text:
    for vowel in vowels:
        if character == vowel:
            text = text.replace(vowel, '')
        else:
            text = text.replace(vowel.upper(), '')

print(text)