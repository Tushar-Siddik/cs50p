import sys
from PIL import Image, ImageOps
import os


def main():
    arg_len = len(sys.argv[1:])
    input_path = ''
    output_path = ''

    if check_argument(arg_len):
        input_path = sys.argv[1]
        output_path = sys.argv[2]

    if check_ext(input_path, output_path):
        try:
            muppet = Image.open(input_path)
            shirt = Image.open("shirt.png")
            shirt_size = shirt.size

            muppet = ImageOps.fit(muppet, size = shirt_size)

            muppet.paste(im = shirt, mask = shirt)

            muppet.save(output_path)

        except FileNotFoundError:
            sys.exit("Input does not exists")


def check_argument(arg):
    if arg < 2:
        sys.exit("Too few command-line arguments")
    elif arg > 2:
        sys.exit("Too many command-line arguments")
    return True


def check_ext(input_file, output_file):
    extensions = {".jpg", ".jpeg", ".png"}
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    if input_ext not in extensions:
        sys.exit("Invalid input")
    elif output_ext not in extensions:
        sys.exit("Invalid output")
    elif input_ext != output_ext:
        sys.exit("Input and Output have different extensions")
    return True


if __name__ == "__main__":
    main()
