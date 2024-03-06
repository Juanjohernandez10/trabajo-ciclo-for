
#un turista realiza un viaje de un punta A  a un punto B, dentro del rango del punto A al punto 	B
#DEBE REALIZAR VARIAS ESCALES LAS CUALES  dependen de el realizar; enseñe un algoritmo que permita 
#ingresar la cantidad de escalas dentro de las cuales el turista debe ingresar las distancia a recorrer 
#e ir sumando cada 1 al final decir cuantas distancias  y etapas realizo 

papa = 0
yuca = 0
zanahoria = 0
tipo =  int( input('1/papa 2/yuca 3/zanahoria: '))
if tipo == 1:
    for i in range(3):
        litros = int(input('cuantos litros gastaste-> '))
        papa += litros
    print(' los litros gastados fueron ', papa)

if tipo == 2:
    for i in range(2):
        litros = int(input('cuantos litros gastaste-> '))
        yuca += litros
    print(' los litros gastados fueron ', yuca)
if tipo == 3:
    for i in range (2):
        litros = int(input('cuantos litros gastaste-> '))