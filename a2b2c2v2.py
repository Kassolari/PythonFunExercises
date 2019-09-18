import random
import math

ran = 10000000000
a,b,f = 1,1,False

print("Podaj liczbe do znalezienia kwadratow liczb sumujacych")
c = int(input())

for i in range (1,ran):
    if i == 0: i=1
    a = i
    for ii in range (1,ran):
        if ii == 0: ii=1
        b = ii
        print("Proba"," ",a," ",b)
        if a**2 + b*b == pow(c,2):
            print("Dla ",c," wyniki to ",a," ",b)
            f = True
            if f == True: break
    if f == True: break
            
    
