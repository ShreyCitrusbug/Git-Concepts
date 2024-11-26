from datetime import date

user_name: str = input("Enter your name : ")
user_age: int = int(input("Enter your age : "))


def calc_100(name: str, age: int) -> None:
    current_year: int = int(date.today().year)
    age_left: int = 100 - age
    year_100: int = current_year + age_left
    print(f"Hello {name}, you will be 100 years old in {year_100} ")


calc_100(user_name, user_age)
