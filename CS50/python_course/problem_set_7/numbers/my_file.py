import sys

def main(ip):
    if validate_ip(ip):
        return True
    return False

def validate_ip(ip):
    numbers = ip.split('.')
    try:
        numbers = [int(i) for i in numbers]
    except ValueError:
        sys.exit(False)
    return True if len([i for i in numbers if 0<=i<=255]) == 4 else False

if __name__ == "__main__":
    ip = input("IPv4 Address: ")
    print(main(ip))