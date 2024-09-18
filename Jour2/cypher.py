
import sys 

alphabet = "abcdefghijklmnopqrstuvwxyz"



def caesar (bool, mot, decalage):
    result = ""
    alphabet_modif=""
    if bool:
        for i in range(len(alphabet)):
            alphabet_modif= alphabet_modif +alphabet[((i+decalage)%(len(alphabet)))] 
        for j in mot:
            result+= alphabet_modif[alphabet.find(j)]

    else:
        for i in range(len(alphabet)):
            alphabet_modif= alphabet_modif +alphabet[((i-decalage)%(len(alphabet)))] 
        for j in mot:
            result+= alphabet_modif[alphabet.find(j)]
    return result

print(caesar(True,"soleil",47))
motinverse=caesar(True,"soleil",47)
print(caesar(False, motinverse,47))


