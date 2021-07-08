#! /usr/bin/python3
#author: Ayushman Agrawal Hingorani
#descripton: This is an application for the conversion of morse code from latin characters and reverse to help people learn more about morse and help them translate with ease
#packages to be used: we need a base gui file that can be used along with this
#developers knowing different languages will also be appreciated in translation of this application and if there is morse/similar to morse in their native language
global morse
morse = {
        ".-": "A",
        "-..." : "B",
        "-.-." : "C",
        "-.." : "D",
        "." : "E",
        "..-." : "F",
        "--." : "G",
        "----" : "H",
        ".." : "I",
        ".---" : "J",
        "-.-" : "K",
        ".-.." : "L",
        "--" : "M",
        "-." : "N",
        "---" : "O",
        ".--." : "P",
        "--.-" : "Q",
        ".-." : "R",
        "..." : "S",
        "-" : "T",
        "..-" : "U",
        "...-" : "V",
        ".--" : "W",
        "-..-" : "X",
        "-.--" : "Y",
        "--.." : "Z",
        "/"    : " ",
        "done" : ""
}

global text
text = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "----",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    }





# This will take the morse and then output a list containing all the morse values
def morse_text():

    output = []
    ascii = input("Please enter the character\n")
    while ascii:
        if ascii.casefold() in morse:
            ab = ascii.casefold()

            if ab == "done":
                break
            else:
                output.append(ascii)
            print(output)
            ascii = input("Please enter the next character\n")

        elif ascii not in morse:
            print("This is not a morse character")
            ascii = input("Please enter the next character\n ")

    return output

# This will convert the morse to text and print the result
def conversion(convert):
    index = 0
    letters = []
    while index >= 0:
        if index <= len(convert)-1:
            a = convert[index]
            b = morse[a]
            letters.append(b)
            index += 1
        else:
            break

    string1 = " "
    index2 = 0
    while index2 >= 0:
        if index2 <= len(letters)-1:
            c = letters[index2]
            string1 = string1+c+""
            index2 += 1

        else:
            print(string1)
            break

list = morse_text()
conversion(list)
