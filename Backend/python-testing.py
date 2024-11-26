from datetime import date

user_name: str = input("Enter your name : ")
user_age: int = int(input("Enter your age : "))


def calc_100(name: str, age: int) -> None:
    year = date.today().year
    year_100: int = year + 100 - age
    print(f"{name} will be 100 years old in the year {year_100}")


calc_100(user_name, user_age)
