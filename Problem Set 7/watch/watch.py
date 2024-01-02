import re
import sys


def main():
    print(parse(input("HTML: ")))


# http://youtube.com/embed/xvFZjo5PgG0
# https://youtube.com/embed/xvFZjo5PgG0
# https://www.youtube.com/embed/xvFZjo5PgG0

def parse(s):
    pattern = r"^\<iframe.+youtube\.com\/embed\/(\w+).*"
    if matches := re.search(pattern, s):
        return f"https://youtu.be/{matches.group(1)}"


if __name__ == "__main__":
    main()
