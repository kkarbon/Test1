


#### ZADANIE 3

def ogon(lista):
    return(lista[1:])

#### ZADANIE 4
## MOŻNA ITEROWAĆ BEZPOŚREDNIO NA LIŚCIE!!!!!!!

def dlugosc(lista):
    wynik = 0
    for i in lista:
        wynik+=1
    return wynik

#### ZADANIE 5



#### ZADANIE 6

# print("Podaj n-ty element listy licząc od zera, nie większy niż:", dlugosc(innalista)-1)

# x = int(input())

def nta(lista, n):
    return(lista[n])

# print(nta(innalista,x))

#### ZADANIE 7
#### Na takiej samej zasadzie działają pozostałe logiczne
#### ŁATWIEJ Z return FALSE  i else return TRUE

(a,b)=(0,0)

def alternatywa(x,y):
    if x == 1 and y == 1:
        return 1
    elif x == 1 and y == 0:
        return 1
    elif x == 0 and y ==1:
        return 1
    elif x==0 and y==0:
        return 0
    else:
        print("Elementy alternatywy nie przyjmują wartości 1 lub 0")

print(alternatywa(a,b))


#zadanie nieistniejące na końcu
