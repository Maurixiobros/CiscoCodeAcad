
primpal = input("Primera palabra: ")
segpal = input("Segunda palabra: ")

primpal = primpal.lower()
segpal = segpal.lower()

primpal = primpal.replace(" ", "")
segpal = segpal.replace(" ", "")

if len(primpal) != len(segpal):
    print("No son anagramas")
else:
    for char in primpal:
        if char not in segpal:
            print("No son anagramas")
            break
    else:
        print("Son anagramas")