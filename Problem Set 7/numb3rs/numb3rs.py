import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    matches = re.search(pattern, ip)
    return chk_range(matches)

def chk_range(regroup):
    for num in range(1,5):
        try:
            return regroup.group(num) <= '255'
        except AttributeError:
            return False

if __name__ == "__main__":
    main()
