expression = input("Expression: ")
digits = expression.split(" ")

match digits[1]:
    case "+":
        print(float(digits[0]) + float(digits[2]))
    case "-":
        print(float(digits[0]) - float(digits[2]))
    case "*":
        print(float(digits[0]) * float(digits[2]))
    case "/":
        print(float(digits[0]) / float(digits[2]))
