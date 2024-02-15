def product(a, b):
    if (a < b):
        return product(b, a)
    elif (b != 0):
        return (a + product(a, b-1))
    else:
        return 0
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print("Произведением двух чисел будет: ", product(a, b))