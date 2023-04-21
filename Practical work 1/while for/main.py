print("Завершити програму - введіть 0")
print("Пошук простого числа") 

while True:
    number = int(input("Введіть число: "))

    if number == 0:
        break
    elif number < 0:
        print("Число не може бути від'ємним")
        continue

    prime = True

    for i in range(2, number):
        if number % i == 0: prime = False

    if prime: print(number, " - це просте число")
    else: print(number, " - це не просте число")