import sys
from PIL import Image, ImageOps


def main():
    args = sys.argv
    valid_args = validate_input(args) #returns a list of the valid input and output
    edit(valid_args)
    sys.exit()

def edit(valid_args):
    u_input, u_output = valid_args

    try:
        with Image.open(u_input) as photo:
            with Image.open("shirt.png") as shirt:

                # resize and crop the photo to match shrt size
                photo = ImageOps.fit(photo, shirt.size)

                # Paste shirt on top of photo since shirt is transparent
                photo.paste(shirt, shirt)

                # saving final image
                photo.save(u_output)

    except FileNotFoundError:
        sys.exit("File does not exist")


def validate_input(args):
    # check for ending extension
    for arg in args[1:]:    #skip the first arg (actual py file)
        ext = arg.split(".")
        if ext[1].lower() not in ["jpeg", "jpg", "png"]:
            sys.exit("Not a valid image file")

    # check for length of arguments
    if len(args) < 3:
        sys.exit("Too few command line arguments")
    elif len(args) > 3:
        sys.exit("Too many command line arguments")
    else:
        # compare user input and output file type for a match
        arg_1_type = args[1].split(".")
        arg_2_type = args[2].split(".")

        if arg_1_type[1].lower() != arg_2_type[1].lower():
            sys.exit("input and output has different extensions")

        # unpack the two needed args
        u_input, u_output = args[1:] #args[1:] takes skips the first argument (the actual py file) and takes the rest

        return [u_input, u_output]


if __name__ == "__main__":
    main()
