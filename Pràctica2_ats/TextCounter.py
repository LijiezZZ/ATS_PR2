"""compta nom閟 una vegada una lletra en una paraula --> cama freq d'a-> 1 cop"""
import sys

def splitting(args):
    
    resultat = []
    
    for filename in args:
        f = open(filename, "r")
        
        for line in f:
            resultat.append(line)
    
    return resultat
    

def mapping(frases):
    
    resultat = {}
    
    for frase in frases:
        paraules = frase.strip().split(" ")
        for paraula in paraules:
            if paraula not in resultat and paraula.isalpha():
                resultat[paraula] = 1
        
    return resultat
            
            

def shuffling():
    return 0

def reducing():
    return 0

def main():
    args = sys.argv[1:]
    
    if len(args) == 0:
        print("Nombre d'argument d'entrada és 0")
        
    else:
        frases = splitting(args)
        freqs = mapping(frases)
        print(freqs)
        

if __name__ == "__main__":
    main();
