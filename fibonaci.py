def fibon(n):
### Funkcja liczaca ciag fibanaciego do liczby podanej w funkcji
    a,b = 0, 1
    while a < n:
        print(a)
        a , b = b, a+b
    
fibon(1000000)