import sys
from PIL import Image, ImageOps


def check_command_line(arg):
    if len(arg) > 3:
        sys.exit("Too many comand-line argument")
    elif len(arg) < 3:
        sys.exit("Too few comand-line argument")
    extentions = [i.split('.')[1] for i in arg if i.split('.')[1] in {'jpeg', 'jpg', 'png'}]
    if len(extentions) != 3:
        sys.exit("Invalid output")
    elif extentions[0] != extentions[2]:
        sys.exit("Input and output have different extensions")

def main():
    check_command_line(sys.argv[1:])
    try:
        imagephoto = Image.open(sys.argv[2])
    except:
        sys.exit("Invalid input")
    t_shirt = Image.open(sys.argv[1])
    size = t_shirt.size
    new_img = ImageOps.fit(imagephoto, size)
    new_img.paste(t_shirt, t_shirt)
    new_img.save(sys.argv[3])



if __name__ == "__main__":
    main()


