text = input("Ingresa un texto: ")

palindrome = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.lower()
    palindrome += char

if palindrome == palindrome[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")