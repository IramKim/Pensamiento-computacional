#formula de Gorostiaga

def calc_1rm(ing_peso,ing_rep):
    rm_1 = ing_peso / (1.0278-(0.0278*ing_rep))
    return rm_1


#datos pedidos

ing_peso = float(input("Ingrese el peso trabajado en kg: "))

ing_rep = int(input("A cuantas repeticiones?: "))

ing_rm = int(input("Que RM quisieras saber? 1-12: "))

#mostrar resultado

pausa = input("presiona ENTER para mostrar resultados")

#coeficientes y formulas

if ing_rm == 1:
    print("tu 1RM es: %.1f"%calc_1rm(ing_peso,ing_rep))
    
elif ing_rm == 2:
    rm = calc_1rm(ing_peso,ing_rep) * 0.95
    print("tu 2RM es: %.1f"%rm)
    
elif ing_rm == 3:
    rm = calc_1rm(ing_peso,ing_rep) * 0.90
    print("tu 3RM es: %.1f"%rm)
    
elif ing_rm == 4:
    rm = calc_1rm(ing_peso,ing_rep) * 0.86
    print("tu 4RM es: %.1f"%rm)

elif ing_rm == 5:
    rm = calc_1rm(ing_peso,ing_rep) * 0.82
    print("tu 5RM es: %.1f"%rm)
    
elif ing_rm == 6:
    rm = calc_1rm(ing_peso,ing_rep) * 0.78
    print("tu 6RM es: %.1f"%rm)
    
elif ing_rm == 7:
    rm = calc_1rm(ing_peso,ing_rep) * 0.74
    print("tu 7RM es: %.1f"%rm)
    
elif ing_rm == 8:
    rm = calc_1rm(ing_peso,ing_rep) * 0.70
    print("tu 8RM es: %.1f"%rm)
    
elif ing_rm == 9:
    rm = calc_1rm(ing_peso,ing_rep) * 0.65
    print("tu 9RM es: %.1f"%rm )
    
elif ing_rm == 10:
    rm = calc_1rm(ing_peso,ing_rep) * 0.61
    print("tu 10RM es: %.1f"%rm)
    
elif ing_rm == 11:
    rm = calc_1rm(ing_peso,ing_rep) * 0.57
    print("tu 11RM es: %.1f"%rm)

elif ing_rm == 12:
    rm = calc_1rm(ing_peso,ing_rep) * 0.53
    print("tu 12RM es: %.1f"%rm)











    


