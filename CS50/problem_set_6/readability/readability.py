from string import ascii_letters

def main(text):
    letter = len([i for i in text if i in ascii_letters])
    words = len(text.split(' '))
    sentences = len([i for i in text if i in "!?."])
    result = 0.0588 * (letter * 100/words) - 0.296 * (sentences * 100/words) - 15.8
    if result >= 16:
        return "Grade 16+"
    elif result < 1:
        return "Before Grade 1"
    else:
        return f'Grade {int(result) if result-int(result) <= 0.5 else int(result)+1}'


if __name__ == "__main__":
    text = input()
    print(main(text))