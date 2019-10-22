# Transcribing DNA into RNA exercise

rnaout = open('rnaout.txt', 'w')

dnastring = input("Please input a DNA sequence to be transcribed: ")


for char in dnastring:
    if char == "T":
        rnaout.write('U')
    else:
        rnaout.write(char)

