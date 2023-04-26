#tutaj jest nowy branch

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
