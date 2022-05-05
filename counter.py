import multiprocessing
import sys
import time
import gc
import re
from multiprocessing import Pool

import numpy


def split(arg):
    
    with open(arg, 'r') as f:
        return (f.readlines())
        

def map(frase):
    
    resultat = []
    
        
    fraseNeta = re.sub("[^\w ]", "", frase.lower())
    
    for paraula in fraseNeta.split():
        aux = {}
        for lletra in list(paraula):
            aux[lletra] = 1
        resultat.append(aux)
    
    return resultat

def reduce(freq_mapped):
    
    resultat = {}
    
    for llista in freq_mapped:
        for dic in llista:
            for key in dic.keys():
                if key not in resultat:
                    resultat[key] = 1
                else:
                    resultat[key] += 1
    
    return resultat
    
def comptarParaules(frase):

    resultat = 0
    
    paraules = re.sub("[^\w ]", "", frase).split()
    resultat += len(paraules)

    return resultat

def map_reduce_parallel(arg):
    
    frases = split(arg)
    
    numParaules = []
    
    with Pool() as p:
        numParaules += p.map(comptarParaules, frases)
        p.close()
    
    numParaules = sum(numParaules)
    
    freq_mapped = []
    
    print(len(frases))
    
    while frases != []:
        with Pool() as p:
            freq_mapped += p.map(map, frases[:5000000])
            p.close()
            
        del frases[:5000000]
    
    del frases
    gc.collect()
    
    freq_reduced = reduce(freq_mapped)
    
    del freq_mapped
    gc.collect()
    
    print(freq_reduced)
    
    print(arg)
    for key, value in freq_reduced.items():
        if key != list(freq_reduced.keys())[-1]:
            print(key, ":", "{:.2%}".format(value / numParaules))
        else:
            print(key, ":", "{:.2%}".format(value / numParaules), "\n")

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
    main()