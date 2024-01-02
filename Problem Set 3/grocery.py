def main():
    grocery_dict = {}
    counter = 1
    while True:
        try:
            item = input().upper()
            if item not in grocery_dict:
                grocery_dict[item] = counter
            else:
                counter += 1
                grocery_dict[item] = counter

        except EOFError:
            dict_sort = dict(sorted(grocery_dict.items()))
            for keys in dict_sort:
                print(dict_sort[keys], keys)
            break


if __name__ == "__main__":
    main()

