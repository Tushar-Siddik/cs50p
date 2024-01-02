def main():
    x = convert(input("Fraction: "))
    print(gauge(x))


# def convert(fraction):
#     while True:
#         try:
#             num1, num2 = fraction.split("/")

#             if num1.isnumeric() and num2.isnumeric():
#                  result = (int(num1) / int(num2))*100
#                  if result > 100:
#                     continue
#                  return round(result)
#             continue

#         except ValueError:
#             pass
#         except ZeroDivisionError:
#             pass


def convert(fraction):
    num1, num2 = fraction.split("/")

    result = (int(num1) / int(num2))*100
    if result > 100:
        raise ValueError

    return round(result)



def gauge(percentage):
    if 0 <= percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    return f"{percentage}%"


if __name__ == "__main__":
    main()
