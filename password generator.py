import random
import string

def generate_password(length):
   
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print(" Strong Password Generator ")
    try:
       
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Error: Password length must be a positive number.")
            return
        
        password = generate_password(length)
        print("\nGenerated Password:")
        print(password)
    except ValueError:
        print("Error: Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
