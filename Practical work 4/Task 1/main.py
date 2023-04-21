text = open('input.txt', 'r', encoding='utf-8')
content = text.read()
text.close()

print()

new = open('count.txt', 'w')

symbols = len(content)

print(symbols)

new.write(str(symbols))
new.close()