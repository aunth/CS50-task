import re

def main(mail):
    return "Valid" if valid(mail) else "Invalid"

def valid(main):
    a = re.findall(r"\w*@\w*\.\w*", main)
    print(a)
    return main in a


if __name__ == "__main__":
    print(main(input()))