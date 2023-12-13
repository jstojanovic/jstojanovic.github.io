import re
# match a 3 digit number
pattern = re.compile(r'\b\d{2}\b')

svi_kandidati = []

with open("ponuda", "r") as file:
    outputFile = open("potraznja", "w")
    datoteka = file.read().split("\n")
    for i, line in enumerate(datoteka):
        if pattern.search(line):
            matching_lines = datoteka[i:i+8]
            svi_kandidati.append(matching_lines)

for kandidat in svi_kandidati:

    print(kandidat) 
    