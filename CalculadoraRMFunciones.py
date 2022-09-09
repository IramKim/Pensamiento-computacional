#formula de Gorostiaga 1RM

def calc_1rm(ing_peso,ing_rep):
    rm_1 = ing_peso / (1.0278-(0.0278*ing_rep))
    return rm_1

#coeficientes y formulas
def calc_rm(ing_rm):
    if ing_rm == 1:
        return("tu 1RM es: %.1f"%calc_1rm(ing_peso,ing_rep))
    
    elif ing_rm == 2:
        rm = calc_1rm(ing_peso,ing_rep) * 0.95
        return("tu 2RM es: %.1f"%rm)
    
    elif ing_rm == 3:
        rm = calc_1rm(ing_peso,ing_rep) * 0.90
        return("tu 3RM es: %.1f"%rm)
    
    elif ing_rm == 4:
        rm = calc_1rm(ing_peso,ing_rep) * 0.86
        return("tu 4RM es: %.1f"%rm)

    elif ing_rm == 5:
        rm = calc_1rm(ing_peso,ing_rep) * 0.82
        return("tu 5RM es: %.1f"%rm)
    
    elif ing_rm == 6:
        rm = calc_1rm(ing_peso,ing_rep) * 0.78
        return("tu 6RM es: %.1f"%rm)
    
    elif ing_rm == 7:
        rm = calc_1rm(ing_peso,ing_rep) * 0.74
        return("tu 7RM es: %.1f"%rm)
    
    elif ing_rm == 8:
        rm = calc_1rm(ing_peso,ing_rep) * 0.70
        return("tu 8RM es: %.1f"%rm)
    
    elif ing_rm == 9:
        rm = calc_1rm(ing_peso,ing_rep) * 0.65
        return("tu 9RM es: %.1f"%rm )
    
    elif ing_rm == 10:
        rm = calc_1rm(ing_peso,ing_rep) * 0.61
        return("tu 10RM es: %.1f"%rm)
    
    elif ing_rm == 11:
        rm = calc_1rm(ing_peso,ing_rep) * 0.57
        return("tu 11RM es: %.1f"%rm)

    elif ing_rm == 12:
        rm = calc_1rm(ing_peso,ing_rep) * 0.53
        return("tu 12RM es: %.1f"%rm)

    else:
        return("Introduce un número valido")

#datos pedidos

ing_peso = float(input("Ingrese el peso trabajado en kg: "))

ing_rep = int(input("A cuantas repeticiones?: "))

ing_rm = int(input("Que RM quisieras saber? 1-12: "))

#mostrar resultado

pausa = input("presiona ENTER para mostrar resultados")
print(calc_rm(ing_rm))










    



