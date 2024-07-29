# A leap year (in the Gregorian calendar) occurs:
#
#     In every year that is evenly divisible by 4.
#     Unless the year is evenly divisible by 100, in which case it's only a leap year if the year is also evenly
#     divisible by 400.
#
# Some examples:
#
#     1997 was not a leap year as it's not divisible by 4.
#     1900 was not a leap year as it's not divisible by 400.
#     2000 was a leap year!

# Instructions
# Your task is to determine whether a given year is a leap year.


def ask_year() -> int:
    while True:
        user_input = input("Enter a year to know whether it is a leap year or not:\n")
        try:
            user_input_int = int(user_input)
            return user_input_int
        except ValueError:
            print(f"{user_input} is not an integer. A year must be an integer number.\n\n")


def is_leap(input: int) -> None:
    if input % 100 == 0:
        if input % 400 != 0:
            return print(f"{input} is not a leap year. It is not evenly divisible by 400.")
        else:
            return print(f"{input} is a leap year. It is evenly divisible by 400.")
    elif input % 4 == 0:
        return print(f"{input} is a leap year. It is evenly divisible by 4.")
    elif input % 4 != 0:
        return print(f"{input} is not a leap year. It is not evenly divisible by 4.")


user_input = ask_year()
is_leap(user_input)
