

def potDyV(x, a):
    if a == 0:
        result = 1
    else:
        if a == 1:
            result = x
        else:
            if a % 2 == 0:
                aux = potDyV(x, a // 2)
                result = aux * aux
            else:
                result = x * potDyV(x, a - 1)
    return result




print("Cálculo de x^a con un enfoque de Divide y Vencerás")
x = float(input("Valor de la x? "))
a = float(input("Valor de la a? "))
print("x^a = ", potDyV(x,a))