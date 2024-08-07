import random
import string

def generatepassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Length should be an integer. ")
        return

    password = generatepassword(length)
    print("Generated password:", password)


if __name__ == "__main__":
    main()
