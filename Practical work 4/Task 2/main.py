file_input = open('input.txt', 'r')

number = int(file_input.readline())

a = []

positive = 0
negative = 0

steamy = 0
odd = 0

maximum = 0
minimum = 0

for i in range(number):
    a.append(int(file_input.readline()))

file_input.close()

for i in range(number):
    if a[i] < 0: positive += 1
    elif a[i] > 0: negative += 1
    
    if a[i] != 0:
        if a[i] % 2 == 0: steamy += 1
        else: odd += 1

    if a[i] > maximum: maximum = a[i]
    if a[i] < minimum: minimum = a[i]

file_output = open('output.txt', 'w')
file_output.write('positive = ')
file_output.write(str(positive))
file_output.write('\nnegative = ')
file_output.write(str(negative))
file_output.write('\n\nsteamy = ')
file_output.write(str(steamy))
file_output.write('\nodd = ')
file_output.write(str(odd))
file_output.write('\n\nmaximum = ')
file_output.write(str(maximum))
file_output.write('\nminimum = ')
file_output.write(str(minimum))
file_output.close()