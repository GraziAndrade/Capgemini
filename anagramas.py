from itertools import permutations

string = str(input("Escreva algo e te direi a quantidade de anagramas pares contidos: "))
anagramas = 0

for g in range(1, len(string)):
    #print("g = "+str(g))
    for i in range(0, len(string) - 1):
        #print(" i = "+str(i))
        pf = set()
        #print("  is = " + string[i:i + g])
        pf.update("".join(f) for f in permutations(string[i:i + g], g))
        for x in pf:
            #print("   x = " + x)
            #print("    xs = " + string[i + 1:len(string)])
            if string[i + 1:len(string)].count(x):
                #print("     xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa = " + x)
                anagramas += 1
print("anagramas = "+str(anagramas))
