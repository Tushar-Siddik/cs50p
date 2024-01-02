import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\bum\b"
    um_list = re.findall(pattern, s, re.IGNORECASE)
    return len(um_list)


if __name__ == "__main__":
    main()
