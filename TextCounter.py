import sys
import re
import time
from multiprocessing import Pool
import gc

def splitting(filename):
    print("SPLITTING")
    
    resultat = []
    
    f = open(filename, "r")
        
    for line in f:
        resultat.append(line.lower())
    
    return resultat
    

def mapping(frase):
    print("MAPPING")
    
    resultat = []
    
    paraules = re.sub("[^\w ]", "", frase).split()

    for paraula in paraules:
        aux = {}
        for lletra in list(paraula):
            if lletra not in aux:
                aux[lletra] = 1
        resultat.append(aux)
        
    return resultat
            
            

def shuffling(freq_mapped):
    print("SHUFFLING")
    
    resultat = {}

    for llista in freq_mapped:
        for dic in llista:
            for key in dic.keys():
                if key not in resultat:
                    resultat[key] = [1]
                else:
                    resultat[key].append(1)

    return resultat
        

def reducing(freq_shuffled):
    print("REDUCING")
    
    resultat = {}

    for key, value in freq_shuffled.items():
        resultat[key] = len(value)

    return resultat

def comptarParaules(frases):
    print("COUNTING WORDS")

    resultat = 0

    for frase in frases:
        paraules = re.sub("[^\w ]", "", frase).split()
        resultat += len(paraules)

    return resultat

def map_reduce(arg):

    frases = splitting(arg)

    num_paraules = comptarParaules(frases)

    freq_mapped = []
    for frase in frases:
        freq_mapped.append(mapping(frase))

    freq_shuffled = {}
    freq_shuffled = shuffling(freq_mapped)
        
    freq_reduced = {}
    freq_reduced = reducing(freq_shuffled)

    print(arg)
    for key, value in freq_reduced.items():
        if key != list(freq_reduced.keys())[-1]:
            print(key, ":", "{:.2%}".format(value / num_paraules))
        else:
            print(key, ":", "{:.2%}".format(value / num_paraules), "\n")

def map_reduce_parallel(arg):

    frases = splitting(arg)

    num_paraules = comptarParaules(frases)

    with Pool() as p:
        freq_mapped = p.map(mapping, frases)
        p.close()

    freq_shuffled = {}
    freq_shuffled = shuffling(freq_mapped)
    
    del freq_mapped
    gc.collect()
    
    freq_reduced = {}
    freq_reduced = reducing(freq_shuffled)
    
    del freq_shuffled
    gc.collect()

    print(arg)
    for key, value in freq_reduced.items():
        if key != list(freq_reduced.keys())[-1]:
            print(key, ":", "{:.2%}".format(value / num_paraules))
        else:
            print(key, ":", "{:.2%}".format(value / num_paraules), "\n")

def main():

    args = sys.argv[1:]
    
    if len(args) == 0:
        print("Nombre d'argument d'entrada és 0")
        
    else:
        for arg in args:
            start_time = time.time()
            map_reduce_parallel(arg)
            end_time = time.time()
            print(end_time - start_time)

if __name__ == "__main__":
    main();
