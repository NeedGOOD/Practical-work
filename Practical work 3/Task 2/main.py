def recursion(word):
    if word == "":
        return ""
    else:
        palindrome = recursion(word[1:])
        palindrome += word[0]
        return palindrome

word = "salas"

duplicate = recursion(word)

if word == duplicate: print("Це паліндром")
else: print("Це не паліндром")