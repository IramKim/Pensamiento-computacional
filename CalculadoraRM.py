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
    acum = 1
    while cont <= ing_rm:
        acum = acum - 0.05
        cont = cont + 1
        return acum  
      
def calc_rm(ing_rm):
    for i in range(0,13):
        if i == ing_rm:
            rm = ((calc_1rm(ing_peso,ing_rep)) * (coeficiente(ing_rm)))
            return("tu", ing_rm, "RM es: %.1f"%rm)
    
def lista(ing_rep,ing_rm,ing_peso):
    lista = [0,0,0]
    for x in lista:
        lista[0] = ing_rep
        lista[1] = ing_rm
        lista[2] = ing_peso
        return ("datos ingresados:",lista)



#datos pedidos

ing_peso = float(input("Ingrese el peso trabajado en kg: "))

ing_rep = int(input("A cuantas repeticiones?: "))

ing_rm = int(input("Que RM quisieras saber? 1-12: "))


#mostrar resultado

pausa = input("presiona ENTER para mostrar resultados")

print(valid())


print(lista(ing_peso,ing_rep,ing_rm))






    





