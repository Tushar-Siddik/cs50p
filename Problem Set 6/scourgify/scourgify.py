import sys
import csv

def main():
    arg_len = len(sys.argv[1:])
    open_file_path = ""
    if check_argument(arg_len):
        argument = sys.argv[1]
        if check_csv(argument):
            open_file_path = argument

    try:
        students = []
        with open(open_file_path) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)

        for student in students:
            student['name'] = student['name'].split(',')
        # print(students[:2])

        save_file_path = sys.argv[2]
        with open(save_file_path, "w") as file:
            # writer = csv.writer(file)
            # writer.writerow(['first', 'last', 'house'])
            writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            for student in students:
                # writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
                # writer.writeheader()
                writer.writerow({'first': student['name'][1].strip(), 'last': student['name'][0].strip(), 'house': student['house']})


    except FileNotFoundError:
        sys.exit(f"Could not read {open_file_path}")

def check_argument(arg):
    if arg < 2:
        sys.exit("Too few command-line arguments")
    elif arg > 2:
        sys.exit("Too many command-line arguments")
    return True

def check_csv(arg):
    if not arg.endswith(".csv"):
        sys.exit("Not a CSV file")
    return True


if __name__ == "__main__":
    main()
