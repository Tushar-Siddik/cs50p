import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})\:?(\d{0,2})[ ]+([A-Z]{2})[ ]+to[ ]+(\d{1,2})\:?(\d{0,2})[ ]+([A-Z]{2})$"
    if matches := re.search(pattern, s):
        h1, m1, d1, h2, m2, d2 = matches.groups()
        h1 = int(chk_hour(int(h1), d1))
        h2 = int(chk_hour(int(h2), d2))

        if not m1:
            m1 = 0
        if not m2:
            m2 = 0

        m1 = int(chk_minute(int(m1)))
        m2 = int(chk_minute(int(m2)))

        return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"
    raise ValueError


def chk_hour(h, d):
    if h < 12 and d == "PM":
        h += 12
        return h
    elif h < 12 and d == "AM":
        return h
    elif h == 12 and d == "PM":
        return h
    elif h == 12 and d == "AM":
        return 0
    raise ValueError


def chk_minute(m):
    if m < 60:
        return m
    raise ValueError


if __name__ == "__main__":
    main()
