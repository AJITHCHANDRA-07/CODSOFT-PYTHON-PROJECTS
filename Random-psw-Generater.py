import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    while True:
        length = int(input("Enter the desired length of the password (or 0 to exit): "))

        if length == 0:
            print("Exiting Password Generator.")
            break

        password = generate_password(length)
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()