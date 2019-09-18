import random
import math

count = 0
a,b = 1,1
ran = 1000000000

print("Podaj liczbe do znalezienia kwadratow liczb sumujacych")
c = int(input())

while a**2 + b*b != pow(c,2):
    a = random.randrange(1,ran)
    #if a == 0: a = random.randrange(-1000,1000)
    b = random.randrange(1,ran)
    #if b == 0: b = random.randrange(-1000,1000)
    print("Proba",count," ",a," ",b)
    count += 1
else:
    print(a,"  ",b,"  ",c)
    
