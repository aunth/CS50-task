import re
import sys


def main(source):
    output = re.findall(r'src=".+youtube\S+"', source)
    if output:
        src = output[0].split('/')[-1][:-1]
        result = f"https://youtu.be/{src}"
        return result
    return None
    


if __name__ == "__main__":
    source = input("HTML: ")
    print(main(source))