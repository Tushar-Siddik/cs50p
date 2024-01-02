def main():
    x = get_result("Fraction: ")
    print(x)

def get_result(prompt):
    while True:
        try:
            x = input(prompt)

            num1, num2 = x.split("/")

            if num1.isnumeric() and num2.isnumeric():
                 result = (int(num1) / int(num2))*100

                 if 0 <= result <= 1:
                      return "E"
                 elif 99 <= result <= 100:
                      return "F"
                 elif result > 100:
                      continue
                 return (f"{round(result)}%")
            continue

        except ValueError:
            pass
        except ZeroDivisionError:
             pass


if __name__ == "__main__":
    main()
