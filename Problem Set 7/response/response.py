import validators

# pip install validator-collection
# https://pypi.org/project/validator-collection/
# or
# pip install validators
# https://github.com/kvesteri/validators



def main():
    print(validate(input("What's your email address? ")))

def validate(email):
    if validators.email(email):
        return "Valid"
    return "Invalid"

if __name__ == "__main__":
    main()
