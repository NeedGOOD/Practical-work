def recursion(numbers):
    if numbers == []:
        return 0
    else:
        sum = recursion(numbers[1:])
        sum += numbers[0]
        return sum

numbers = [1, 2, 3, 4, 5]

print("Sum = ", recursion(numbers), sep="")