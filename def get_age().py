
def get_age():
    age = int(input("Please enter your age: "))
    if (age >= 18):
        return int(age)
    else:
        return 0

def main():
    age = get_age()
    if (age >= 18):
        print("You are ",age," years old and eligible.")
    else:
        print("Invalid input. You must be at least 18 years old.")
        
if __name__ == "__main__":
    main()
