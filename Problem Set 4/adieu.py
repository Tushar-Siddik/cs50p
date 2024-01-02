import inflect

p = inflect.engine()

# mylist = p.join(("apple", "banana", "carrot"), final_sep="")
# "apple, banana and carrot"

def main():
    name_list = []
    while True:
        try:
            name = input("Name: ")
            if name != " ":
                name_list.append(name)
        except EOFError:
            # name_list = ["fdg", "df", "rt", "dw"]
            mod_name_list = p.join(name_list, final_sep=",")
            print (f"Adieu, adieu, to {mod_name_list}")
            break

if __name__ == "__main__":
    main()
