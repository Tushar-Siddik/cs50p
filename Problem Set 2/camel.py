def main():
    camel_case_name = input("camelCase: ")
    snake_case_name = camel_to_snake(camel_case_name)
    print(f"snake_case: {snake_case_name}")


def camel_to_snake(name):
    result = [name[0].lower()]
    for char in name[1:]:
        if char.isupper():
            result.extend(['_', char.lower()])
        else:
            result.append(char)
    return ''.join(result)


if __name__ == "__main__":
    main()
