import sys
import random

# This will only work in IDLE, it won't work from a command prompt
try:
    shell_connect = sys.stdout.shell
except AttributeError:
    print("idlecolours highlighting only works with IDLE")
    exit()

# Map the colour strings to IDLE highlighting
USE_CUSTOM_COLOURS = False       # Change to True if you want to use custom colours

#Damn American programing, hard coding the amrican spelling into a variable
global colormap

colormap = {"red": "COMMENT",
                "orange": "KEYWORD",
                "green": "STRING",
                "blue": "stdout",
                "purple": "BUILTIN",
                "black": "SYNC",
                "brown": "console"}

# ---------------------------
# Functions
# ---------------------------

# Like the print() function but will allow you to print colours
def printc(text, end="\n"):
    # Parse the text provided to find {text:color} and replace with the colour. Any text not encompassed in braces
    # will be printed as black by default.
    buff = ""
    for char in text:
        if char == "{":
            # Write current buffer in black and clear
            shell_connect.write(buff, colormap["black"])
            buff = ""
        elif char == "}":
            # Write current buffer in color specified and clear
            tag_write = buff.split(":")
            shell_connect.write(tag_write[0], tag_write[1])
            buff = ""
        else:
            # Add this char to the buffer
            buff += char

    # Write the chosen end character (defaults to newline like print)
    sys.stdout.write( end )


# Individual colour functions
def red(text):
    return "{"+ text + ":" + colormap["red"] + "}"

def orange(text):
    return "{"+ text  + ":" + colormap["orange"] + "}"

def green(text):
    return "{"+ text + ":" + colormap["green"] + "}"

def blue(text):
    return "{"+ text  + ":" + colormap["blue"] + "}"

def purple(text):
    return "{"+ text + ":" + colormap["purple"] + "}"

def black(text):
    return "{"+ text  + ":" + colormap["black"] + "}"

def brown(text):
    return "{"+ text + ":" + colormap["brown"] + "}"

def randcol(text):
    color = random.choice(list(colormap.keys()))
    return "{"+ text + ":" + colormap[color] + "}"


