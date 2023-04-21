def is_primitive(number):
    if number <= 1:
        return False
    for d in range(2, number):
        if number % d == 0:
            return False
    return True


print("Введите число от 0 до 1000:")
if is_primitive(int(input())):
    print("Это Простое число")
else:
    print("Это составное число")