import sys
import re

def main(time):
    return convert(time)

def convert(time):
    result = []
    time = time.split(' ')
    if len(time) < 5 or time[2] != 'to':
        sys.exit("Value Error")
    for j, i in enumerate(time):
        if ":" in i:
            numbers = i.split(':')
            if int(numbers[0]) > 11 or int(numbers[1]) > 59:
                sys.exit("Value Error")
            else:
                if time[j+1] == 'AM':
                    result.append(f"0{numbers[0]}:{numbers[1]}" if int(numbers[0])<10 else f"{numbers[0]}:{numbers[1]}")
                else:
                    result.append(f"{int(numbers[0])+12}:{numbers[1]}")
        elif i in [str(i) for i in range(1, 11)]:
            if time[j+1] == 'AM':
                result.append(f"{i}:00" if int(i) > 9 else f"0{i}:00")
            else:
                result.append(f"{int(i)+12}:00")
    return f"{result[0]} to {result[1]}"
    

if __name__ == "__main__":
    input = input("Type your work time: ")
    print(main(input))