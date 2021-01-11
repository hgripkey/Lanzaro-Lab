import os
import sys


def fasta_parse_to_allele(file_in):
    with open(file_in,'r') as file:
        data = file.readlines()
        
    #print(len(data))
    file_out = file_in.split(".fasta")[0] + "_alleles.fasta"
    #print(file_out)
    
    with open(file_out,'w') as file:        
        
        #Duplicate
        for i in range(2):
            for j in data:
                if i == 0:
                    if j[0] == ">":
                        #input(j)
                        file.write(j)
                        
                    else:
                        temp = list(j)
                        for k in range(len(temp)):
                            if temp[k].upper() == 'M':
                                temp[k] = 'A'
                            elif temp[k].upper() == 'R':
                                temp[k] = 'A'
                            elif temp[k].upper() == 'W':
                                temp[k] = 'A'
                            elif temp[k].upper() == 'S':
                                temp[k] = 'C'
                            elif temp[k].upper() == 'Y':
                                temp[k] = 'C'
                            elif temp[k].upper() == 'K':
                                temp[k] = 'G'
                        temp = "".join(temp)
                        file.write(temp)
                else:
                    if j[0] == ">":
                        j = j.split("\n")[0] + "_Second"
                        j = j+'\n'
                        file.write(j)
                    else:
                        temp = list(j)
                        for k in range(len(temp)):
                            if temp[k].upper() == 'M':
                                temp[k] = 'C'
                            elif temp[k].upper() == 'R':
                                temp[k] = 'G'
                            elif temp[k].upper() == 'W':
                                temp[k] = 'T'
                            elif temp[k].upper() == 'S':
                                temp[k] = 'G'
                            elif temp[k].upper() == 'Y':
                                temp[k] = 'T'
                            elif temp[k].upper() == 'K':
                                temp[k] = 'T'
                        temp = "".join(temp)
                        file.write(temp)
        

file_in = input("File: ")
try:
    fasta_parse_to_allele(file_in) 
    
except:
    raise