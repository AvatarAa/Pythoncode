
def get_age(birth_date: int, current_year: int = 2024) -> int:
    """
    Calculates the user's age based on their birth year and the current year.

    :param birth_date: The user's birth year as an integer.
    :param current_year: The current year as an integer (defaults to 2024).
    :return: The user's age as an integer.
    """
    if not isinstance(birth_date, int) or birth_date > 2006:
        raise ValueError("Birth date must be a valid year after 2006.")

    age = current_year - birth_date
    return age


name = input("What is your name? ")
print(f"Hello, {name}!")

while True:
        birth_date = int(input("Please enter your birth year : "))
        if birth_date > 2006:
            print("not allowed entry.")
        elif birth_date < 2006:
            print("you are allowed entry")
        else:
            print("You need to confirm your age.")
            confirmation = input("Is this your right age? (yes/no): ")
            if confirmation.lower() == "yes":
               print("You are allowed to enter.")

            current_year = 2024
            age = get_age(birth_date, current_year)
            print(f"You are {age} years old this {current_year} congrats your old.")
            break