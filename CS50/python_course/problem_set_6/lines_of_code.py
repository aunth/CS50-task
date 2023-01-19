import sys


def chenk_commandline_arguments(a):
        if len(a) > 2:
            return "Too many arguments"
        elif len(a) == 1:
            return "Too few arguments"

def main():
    result = chenk_commandline_arguments(sys.argv)
    if result:
        return result
    file = sys.argv[1]
    if file.split(".")[1] != 'py':
        print("This isn't python file")
    else: 
        try: 
            with open(file) as file1:
                print(len(file1.readlines()))
        except FileNotFoundError:
            print("File doesn't exist")




main()