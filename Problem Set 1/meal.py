def main():
    time = input("What time is it? ")

    if 19 >= convert(time) >= 18:
        print("dinner time")
    elif 13 >= convert(time) >= 12:
        print("lunch time")
    elif 8 >= convert(time) >= 7:
        print("breakfast time")


# def convert(time):
#     hours, minutes  = time.split(":")
#     time = float(hours) + float(minutes) / 60
#     return time

def convert(time):
    if ".m" in time:
        time, ampm = time.split(" ")
        hours, minutes = time.split(":")
        if ampm == "p.m.":
            hours = float(hours) + 12
            return (float(hours) + float(minutes) / 60)

    hours, minutes  = time.split(":")
    time = float(hours) + float(minutes) / 60
    return time


if __name__ == "__main__":
    main()
