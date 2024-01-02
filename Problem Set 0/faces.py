def convert():
    text = input()
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

print(convert())
