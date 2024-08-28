# Exercise 0: Example


def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")


# Call the function
print_greeting()


# Exercise 1: Vowel or Consonant


def check_letter():
    # Your control flow logic goes here
    letter = input("Enter a vowel or a consonant : ")

    if letter in ("a", "e", "i", "o", "u"):
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")


# Call the function
check_letter()


# Exercise 2: Old enough to vote?


def check_voting_eligibility():
    # Your control flow logic goes here
    age = input("Please enter your age : ")

    if int(age) < 16:
        print("Not eligible to vote")
    elif int(age) >= 16:
        print("Eligible to vote")


# Call the function
check_voting_eligibility()


# Exercise 3: Calculate Dog Years


def calculate_dog_years():
    # Your control flow logic goes here
    dogAge = input("Input a dog's age : ")

    if int(dogAge) < 1:
        print("Invalid age!!")
    elif int(dogAge) == 1:
        print("your dog is 10 years old")
    elif int(dogAge) == 2:
        print("your dog is 20 years old")
    elif int(dogAge) > 2:
        print(f"your dog is {20+(7*(int(dogAge)-2))} years old")


# Call the function
calculate_dog_years()


# Exercise 4: Weather Advice


def weather_advice():
    # Your control flow logic goes here
    weather = input("Weather is cold? (yes/no) :").lower()
    raining = input("Is it raining? (yes/no) :").lower()

    if weather == "yes" and raining == "yes":
        print("Wear a waterproof coat.")
    elif weather == "yes" and raining == "no":
        print("Wear a warm coat.")
    elif weather == "no" and raining == "yes":
        print("Carry an umbrella.")
    elif weather == "no" and raining == "no":
        print("Carry an umbrella.")
    else:
        print("Are you in a CAVE!!")


# Call the function
weather_advice()


# Exercise 5: What's the Season?


def determine_season():
    month = input("Enter the month of the year (Jan - Dec) : ").lower()
    day = int(input("Enter the day of the month : "))

    if month in ("dec", "jan", "mar"):
        if month == "dec" and day >= 21:
            print(f"{month} {day} is in Winter.")
        elif month == "jan" and day >= 1:
            print(f"{month} {day} is in Winter.")
        elif month == "mar" and day >= 1 and day < 20:
            print(f"{month} {day} is in Winter.")

    elif month in ("mar", "apr", "may", "jun"):
        if month == "mar" and day >= 20:
            print(f"{month} {day} is in Spring.")
        elif month == "apr" and day >= 1:
            print(f"{month} {day} is in Spring.")
        elif month == "may" and day >= 1:
            print(f"{month} {day} is in Spring.")
        elif month == "jun" and day >= 1 and day < 21:
            print(f"{month} {day} is in Spring.")

    elif month in ("jun", "jul", "aug", "sep"):
        if month == "jun" and day >= 21:
            print(f"{month} {day} is in Summer.")
        elif month == "jul" and day >= 1:
            print(f"{month} {day} is in Summer.")
        elif month == "aug" and day >= 1:
            print(f"{month} {day} is in Summer.")
        elif month == "sep" and day >= 1 and day < 22:
            print(f"{month} {day} is in Summer.")

    elif month in ("sep", "oct", "nov", "dec"):
        if month == "sep" and day >= 22:
            print(f"{month} {day} is in Fall.")
        elif month == "oct" and day >= 1:
            print(f"{month} {day} is in Fall.")
        elif month == "nov" and day >= 1:
            print(f"{month} {day} is in Fall.")
        elif month == "dec" and day >= 1 and day < 21:
            print(f"{month} {day} is in Fall.")


# Your control flow logic goes here

# Call the function
determine_season()

# This 5th one I did my self not Chatgpt .. hahaha
