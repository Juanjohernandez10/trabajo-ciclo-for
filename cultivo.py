

#un agricultor realiza la siembra de 3 cultivos papa, yuca y zanahoria; el cultivo de papa requiere una 
#cantidad X de riego a la semana, la yuca y la zanahoria tambien. consuultaren internet dicho procedimiento y establecer esta crcteristica en un programa 

#litros de agua: cuantos litros de agua 



RIEGO_PAPA = 2
RIEGO_YUCA = 15
RIEGO_ZANAHORIA = 8

NOMBRES_CULTIVOS = ["papa", "yuca", "zanahoria"]

CANTIDAD_RIego = [RIEGO_PAPA, RIEGO_YUCA, RIEGO_ZANAHORIA]

for i in range(len(NOMBRES_CULTIVOS)):
    cantidad_plantas = int(input("Ingrese la cantidad de plantas de " + NOMBRES_CULTIVOS[i] + ": "))
    CANTIDAD_RIego[i] *= cantidad_plantas

for i in range(len(NOMBRES_CULTIVOS)):
    print("La cantidad de riego necesaria para las plantas de " + NOMBRES_CULTIVOS[i] + " es: " + str(CANTIDAD_RIego[i]) + " litros por semana.")