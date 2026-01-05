# import and initialize the needed libraries
from pyfiglet import Figlet
import sys
import random

fig = Figlet()
available = fig.getFonts()

# when no argument is supplied, generate a random font instead
if len(sys.argv) == 1:
    fig.setFont(font=random.choice(available))
    text = input("Input: ")
    print(fig.renderText(text))
    sys.exit(0)

# correct fomat to check arguments
if len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    fontname = sys.argv[2]

    # if font is valid, use it
    if fontname in available:
        fig.setFont(font=fontname)
        text = input("Input: ")
        print(fig.renderText(text))
        sys.exit(0)

    # print error for invalid fon
    print("Invalid usage")
    sys.exit(1)

# All other errors exit silently
sys.exit(1)
