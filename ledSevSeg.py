#Led 7 segmentos

ledoff = ' '
ledon = '#'

#Numero uno
uno = ((ledoff + ledoff + ledon +'\n')*5)

#Numero dos
dos =(ledon*3+'\n'+ ledoff + ledoff + ledon + '\n'+ ledon*3+'\n'+ledon + ledoff + ledoff + '\n'+ ledon*3+'\n')

#Numero tres
tres = (ledon*3+'\n'+ ledoff + ledoff + ledon + '\n'+ ledon*3+'\n'+ ledoff + ledoff + ledon + '\n'+ ledon*3+'\n')

#Numero cuatro
cuatro = (ledon + ledoff + ledon +'\n'+ ledon + ledoff + ledon +'\n'+ ledon*3+'\n'+ ledoff + ledoff + ledon + '\n'+ ledoff + ledoff + ledon + '\n')

#Numero cinco
cinco = (ledon*3+'\n'+ ledon + ledoff + ledoff + '\n'+ ledon*3+'\n'+ ledoff + ledoff + ledon + '\n'+ ledon*3+'\n')

#Numero seis
seis = (ledon*3+'\n'+ ledon + ledoff + ledoff + '\n'+ ledon*3+'\n'+ ledon + ledoff + ledon + '\n'+ ledon*3+'\n')

#Numero siete
siete = ledon*3+'\n'+(ledoff + ledoff + ledon +'\n')*4

#Numero ocho
ocho = (ledon*3+'\n'+ ledon + ledoff + ledon +'\n'+ ledon*3+'\n'+ ledon + ledoff + ledon + '\n'+ ledon*3+'\n')

#Numero nueve
nueve = (ledon*3+'\n'+ ledon + ledoff + ledon +'\n'+ ledon*3+'\n'+ ledoff + ledoff + ledon + '\n'+ ledoff + ledoff + ledon + '\n')

#numero cero
cero = (ledon*3+'\n'+ (ledon + ledoff + ledon +'\n')*3+ ledon*3+'\n')

print("Escribe un numero del 0 al 9: ")
num = input()
if num == '0':
    print(cero)
elif num == '1':
    print(uno)
elif num == '2':
    print(dos)
elif num == '3':
    print(tres)
elif num == '4':
    print(cuatro)
elif num == '5':
    print(cinco)
elif num == '6':
    print(seis)
elif num == '7':
    print(siete)
elif num == '8':
    print(ocho)
elif num == '9':
    print(nueve)

#combinacion de numeros
else:
    for i in num:
        if i == '0':
            print(cero)
        elif i == '1':
            print(uno)
        elif i == '2':
            print(dos)
        elif i == '3':
            print(tres)
        elif i == '4':
            print(cuatro)
        elif i == '5':
            print(cinco)
        elif i == '6':
            print(seis)
        elif i == '7':
            print(siete)
        elif i == '8':
            print(ocho)
        elif i == '9':
            print(nueve)
            

    
