# print(tabulate(table, headers, tablefmt="grid"))
# print(tabulate([["Name","Age"],["Alice",24],["Bob",19]], headers="firstrow"))

import sys
import csv

from tabulate import tabulate

def main():
    arg_len = len(sys.argv[1:])
    file_path = ""
    if check_argument(arg_len):
        argument = sys.argv[1]
        if check_csv(argument):
            file_path = argument

    try:
        pizzas = []
        list_format = []
        with open(file_path) as file:
            reader = csv.DictReader(file)
            for row in reader:
                pizzas.append(row)
            list_key = list(pizzas[0].keys())
            list_format.append(list_key)
            for pizza in pizzas:
                list_val = list(pizza.values())
                list_format.append(list_val)
            # print(list_format)

        print(tabulate(list_format, headers="firstrow", tablefmt="grid"))



    except FileNotFoundError:
        sys.exit("File does not exist")

def check_argument(arg):
    if arg < 1:
        sys.exit("Too few command-line arguments")
    elif arg > 1:
        sys.exit("Too many command-line arguments")
    return True

def check_csv(arg):
    if not arg.endswith(".csv"):
        sys.exit("Not a CSV file")
    return True


if __name__ == "__main__":
    main()

