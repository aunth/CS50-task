from datetime import *
import inflect


def validator(input): # FIXME something went wrong in this func AND realize another question in the course
    try:
        user_birthday = date.fromisoformat(input)
    except ValueError:
        return False
    return user_birthday 

def count_minute(days):
    p = inflect.engine()
    return f"{p.number_to_words(days * 24 * 60)} minutes"
    

def main():
    user_birthday = input("Type your birthday in YYYY-MM-DD format: ")
    respone = validator(user_birthday)
    if respone:
        today = date.today()
        day = today - respone
        print(day)
        result = count_minute(day.days)
    else:
        print("invalid data")
    return result


if __name__ == "__main__":
    print(main())




