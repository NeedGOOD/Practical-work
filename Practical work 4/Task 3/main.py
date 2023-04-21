file_input = open('input.txt', 'r')
text = file_input.read()
file_input.close()

print("Пошук символа")
search = input("~ ")

upperCase = 0
lowerCase = 0

symbols = len(text)
count = 0

for i in range(symbols):
    if 'A' <= text[i] and 'Z' >= text[i]: upperCase += 1
    if 'a' <= text[i] and 'z' >= text[i]: lowerCase += 1

for i in text:
    if search == i: count += 1

file_output = open('output.txt', 'w')
file_output.write('Upper case = ')
file_output.write(str(upperCase))
file_output.write('\nLower case = ')
file_output.write(str(lowerCase))
file_output.write('\n\nCount = ')
file_output.write(str(count))
file_output.close()