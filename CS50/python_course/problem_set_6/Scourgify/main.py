import sys
import csv


def main():
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif len(sys.argv) in {1, 2}:
        sys.exit("Too few arguments")
    else:
        try: 
            with open(sys.argv[1]) as reader:
                with open(sys.argv[2], 'w') as writer:
                    reader = csv.DictReader(reader)
                    fild_heads = ['first', 'last', 'house']
                    writer = csv.DictWriter(writer, fieldnames=fild_heads)
                    writer.writeheader()
                    for row in reader:
                        row['first'] = row['name'].split(', ')[1]
                        row['last'] = row['name'].split(', ')[0]
                        del row['name']
                        writer.writerow(row)
        except FileExistsError:
            print(f"Could not read {sys.argv[1]}")
        except FileNotFoundError:
            print("File doesn't exist")   

main()

