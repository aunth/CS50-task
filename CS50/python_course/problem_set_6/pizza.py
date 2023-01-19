import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) > 2:
        print("Too many arguments")
    elif len(sys.argv) == 1:
        print("Too few arguments")
    else:
        try:
            file = open(sys.argv[1])
            file = [row for row in csv.reader(file)]
            print(tabulate(file[1:], headers=file[0], tablefmt="grid"))
        except FileNotFoundError:
            print("File doesn't exist")


main()

        