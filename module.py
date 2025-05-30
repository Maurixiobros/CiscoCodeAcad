
#!/usr/bin/env python3

__counter = 0

def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum

def prodl(the_list):
    global __counter
    __counter += 1
    the_prod = 1
    for element in the_list:
        the_prod *= element
    return the_prod

if __name__ == "__main__":
    print("Prefiero ser un modulo, pero puedo hacer unas pruebas si me ejecutan")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)