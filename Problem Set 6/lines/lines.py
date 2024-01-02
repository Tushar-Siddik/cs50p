import sys

# arg_len = len(sys.argv[1:])

def main():
    arg_len = len(sys.argv[1:])
    file_path = ""
    if check_argument(arg_len):
        argument = sys.argv[1]
        if check_py(argument):
            file_path = argument

    try:
        with open(file_path) as file:
            total_line = 0
            total_comment_blank = 0

            for line in file:
                total_line += 1
                # if line.startswith("# ") or line.strip() == "":
                #     total_comment_blank += 1

                line = line.lstrip()
                if line.startswith("# ") or line == "":
                    total_comment_blank += 1

            print(total_line - total_comment_blank)

    except FileNotFoundError:
        sys.exit("File does not exist")

def check_argument(arg):
    if arg < 1:
        sys.exit("Too few command-line arguments")
    elif arg > 1:
        sys.exit("Too many command-line arguments")
    return True

def check_py(arg):
    if not arg.endswith(".py"):
        sys.exit("Not a Python file")
    return True


if __name__ == "__main__":
    main()
