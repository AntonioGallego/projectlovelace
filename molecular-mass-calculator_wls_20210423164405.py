import csv
import re
ELEMS={}
with open('periodic_table.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        ELEMS[row[0]]=row[1]

def molecular_mass(chemical_formula):
    mass = 0        
    chemicals = re.findall('[A-Z][^A-Z]*', chemical_formula)
    print("[+] Scanning ",chemicals)
    for chem in chemicals:
        print("  [+]  Analyzing ",chem)
        if len(chem)==1:
            mass+=float(ELEMS[chem])
        elif chem[1].isdigit():
            try:
                mul = float(chem[1:])
            except ValueError:
                mul = 1
            mass += float(ELEMS[chem[0]]) * mul
        else:
            try:
                mul = float(chem[2:])
            except ValueError:
                mul = 1
            mass += float(ELEMS[chem[:2]]) * mul
    return mass