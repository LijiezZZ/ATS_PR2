# -*- coding: utf-8 -*-
import sys
import re


def splitting(args):
    
    resultat = []
    
    for filename in args:
        f = open(filename, "r")
        
        for line in f:
            resultat.append(line.lower())
    
    return resultat
    

def mapping(frase):
    
    resultat = []
    
    paraules = re.sub("[^\w ]", "", frase).split()
    for paraula in paraules:
        aux = {}
        lletres = list(paraula)
        for lletra in lletres:
            if lletra not in aux:
                aux[lletra] = 1
        resultat.append(aux)
        
    return resultat
            
            

def shuffling(freq_map):
    resultat = {}
    
    for llista in freq_map:
        for dic in llista:
            for key in dic.keys():
                if key not in resultat:
                    resultat[key] = [1]
                else:
                    resultat[key].append(1)
    return resultat
        

def reducing(freq_shuffled):
    resultat = {}
    
    for key, value in freq_shuffled.items():
        resultat[key] = len(value)
    
    return resultat

def map_reduce():
    return 0

def main():
    args = sys.argv[1:]
    
    if len(args) == 0:
        print("Nombre d'argument d'entrada és 0")
        
    else:
        frases = splitting(args)
        freq_map = []
        for frase in frases:
            freq_map.append(mapping(frase))
        freq_shuffled = {}
        freq_shuffled = shuffling(freq_map)
        print(freq_shuffled)
        
        freq_reduced = {}
        freq_reduced = reducing(freq_shuffled)
        
        num_lletres = 0
        for value in freq_reduced.values():
            num_lletres += value
        print(num_lletres)
        """676"""
        print(len(freq_reduced.keys()))
        print(freq_reduced['t']/29)
        

if __name__ == "__main__":
    main();
