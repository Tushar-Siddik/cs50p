months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    date = get_date("Date: ")
    print(date)

def get_date(prompt):
    while True:
        date = input(prompt).strip()
        if date[0].isnumeric():
            if "/" in date:
                month, day, year = date.split("/")
                if check_length(day, month):
                    return (convert_date(day, month, year))
                continue
            continue

        else:
            if "," in date:
                month, day, year = date.split(" ")
                day = day.replace(",","")
                if month in months:
                    month = months.index(month) + 1
                    if check_length(day, month):
                        return (convert_date(day, month, year))
                    continue
                continue
            continue


def check_length(day, month):
    return (int(day) <= 31 and int(month) <= 12)


def convert_date(day, month, year):
    return f"{year}-{int(month):02}-{int(day):02}"


if __name__ == "__main__":
    main()
