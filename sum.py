def product(a, b):
    if (a < b):
        return product(b, a)
    elif (b != 0):
        return (a + product(a, b-1))
    else:
        return 0
a = int(input("Diведите первое число: "))
b = int(input("Diведите второе число: "))
print("Произведением двух чисел будет: ", product(a, b))