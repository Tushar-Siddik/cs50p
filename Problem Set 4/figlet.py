import random
import sys
from pyfiglet import Figlet


# fonts = figlet.getFonts()
# print(type(fonts), len(fonts))
# type: LIST, length: 549

# You can set the font with code like this, wherein f is the font’s name as a str:
# figlet.setFont(font=f)

# you can output text in that font with code like this, wherein s is that text as a str:
# print(figlet.renderText(s))


# figlet = Figlet()
fonts = Figlet().getFonts()

def main():
    text = output_function("Input: ")
    print(text)

def output_function(prompt):
    if len(sys.argv) == 1:
        text = input_function(prompt)
        rand_choice = random.choice(fonts)
        f = Figlet(font= rand_choice )
        return(f.renderText(text))

    elif len(sys.argv) == 3 and sys.argv[2] in fonts:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            text = input_function(prompt)
            # f = random.choice(fonts)
            f = Figlet(font = sys.argv[2])
            return(f.renderText(text))

        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")


def input_function(prompt):
    return input(prompt)


if __name__ == "__main__":
    main()
