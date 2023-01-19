import re


def main(text):
    return count(text)

def count(text):
    coun = re.findall(r"\b\W*um\b\W*", text, re.IGNORECASE)
    return len(coun)
    

if __name__ == "__main__":
    print(main(input()))