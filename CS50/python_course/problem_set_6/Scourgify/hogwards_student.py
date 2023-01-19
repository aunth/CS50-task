import sys
from tabulate import tabulate
import csv

def main():
    with open(sys.argv[1]) as file:
        csv_file = csv.reader(file)
        print(tabulate(csv_file, tablefmt="grid"))
    


if __name__ == "__main__":
    main()