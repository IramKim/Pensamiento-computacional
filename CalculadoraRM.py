#formula de Gorostiaga 1RM

def calc_1rm(ing_peso,ing_rep):
    rm_1 = ing_peso / (1.0278-(0.0278*ing_rep))
    return rm_1

#coeficientes y formulas

def valid():
    while ing_rm <= 12:
        return (calc_rm(ing_rm))
    else:
        return ("Introduce un numero valido")
    
def coeficiente(ing_rm):
    cont = 1
    acum = 1.05
    while cont <= ing_rm:
        acum = acum - 0.05
        cont = cont + 1
    return acum  
      
def calc_rm(ing_rm):
    for i in range(0,13):
        if i == ing_rm:
            rm = ((calc_1rm(ing_peso,ing_rep)) * (coeficiente(ing_rm)))
            return("tu", ing_rm, "RM es: %.1f"%rm)

def calc_rms_todos():
    i = 1
    cont = 0
    acum = 1.05
    lista_rm = list(range(1,13))
    lista_res = []
    for x in lista_rm:
        acum = acum - 0.05
        rm = ((calc_1rm(ing_peso,ing_rep)) * acum)
        i = i + 1
        lista_res.append(rm)
    return lista_res


def lista_rms(ing_rep,ing_peso):
    lista = [ing_rep,ing_peso]
    lista_rm = (list(range(1,13)))
    lista_res = calc_rms_todos()
    i = 0
    cont = 0
    print ("Considerando",lista[1],"kg","a",lista[0],"repeticion/es \n")
    while i <= 12:
        for x in lista_rm:
            print ("Tu",lista_rm[i],"RM seria: %.1f"%lista_res[i],)
            i = i + 1
        break
    print("")
    
def tabla_de_equivalencias():
    matrix = []
    lista= [1,5,10,20,30]
    i = 0
    print("Tabla de equivalencias")
    for x in lista:
        columna = []
        columna.append(lista[i])
        columna.append("Kg Es =")
        columna.append(lista[i]*2.2)
        columna.append("Lb")
        i = i + 1
        matrix.append(columna)
    print(matrix)
                

#datos pedidos

ing_peso = float(input("Ingrese el peso trabajado en kg: "))

ing_rep = int(input("A cuantas repeticiones?: "))

ing_rm = int(input("Que RM quisieras saber? 1-12: "))

#mostrar resultado

print("")

pausa = input("presiona ENTER para mostrar resultados")

print("")

print(valid())

print("")

pausa = input("Quieres conocer otros resultados? presiona ENTER ")

print("")

(lista_rms(ing_rep,ing_peso))

print("""NOTA: La calculadora no puede calcular los RM reales que sean mayores al número de repeticiones ingresado, debido
a que ese número de repeticiones esta siendo considerado usando el 100% de la capacidad de tu cuerpo para generar fuerza,
este programa es idoneo para conocer RMs menores que 5, no mayores.

Ej = no es coherente que el 12 RM de 60kg a 12 repeticiones sea menor que 60kg.""","\n")

tabla_de_equivalencias()







    









