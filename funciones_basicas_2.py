def countdown(numero):
    lista = []
    for i in range(numero, -1, -1):
        lista.append(i)
    return lista


resultado = countdown(5)
print(resultado)

print("----")

lista = [1,2]

def imprimir_y_devolver(lista):
    print(lista[0])
    return(lista[1])

print(imprimir_y_devolver(lista))

print("----")

lista = [1,2,3,4,5]

def primero_mas_longitud(lista):
    return(lista[0]+ len(lista))

print(primero_mas_longitud(lista))

print("----")

lista = [5,2,3,2,1,4]
def valores_mayores_que_el_segundo(lista):
    nuevalista = []
    for i in range (0,len(lista),1):
        if i >= lista[2]:
            nuevalista.append(i)
    if len(nuevalista) < 2:
        return False
    print(len(nuevalista))
    return(nuevalista)

print(valores_mayores_que_el_segundo(lista))

print("----")

lista = [1,2,3]
def valores_mayores_que_el_segundo(lista):
    nuevalista = []
    for i in range (0,len(lista),1):
        if i >= lista[2]:
            nuevalista.append(i)
    if len(nuevalista) < 2:
        return False
    print(len(nuevalista))
    return(nuevalista)

print(valores_mayores_que_el_segundo(lista))

print("----")

def length_and_value(a,b):
    lista = []
    for i in range (0,a):
        lista.append(b)
    return(lista)
    
print(length_and_value(4,7))
print(length_and_value(6,2))