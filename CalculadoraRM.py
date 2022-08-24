import math

#datos pedidos

peso = float(input("Ingrese el peso trabajado en kg: "))

rep = int(input("A cuantas repeticiones?: "))

#mostrar resultado

pausa = input("presiona ENTER para mostrar resultados")

#formulas y coeficientes

if rep == 12:
    res_12 = (peso / 0.53)
    res_12_lb = int(res_12 * 2.20462)
    print("Tu 1RM es: %.1f" %res_12, "kg", "o", res_12_lb, "lb")
        

if rep == 11:
    res_11 = (peso / 0.57)
    res_11_lb = int(res_11 * 2.20462)
    print("Tu 1RM es: %.2f" %res_11, "kg", "o", res_11_lb, "lb")

if rep == 10:
    res_10 = (peso / 0.61)
    res_10_lb = int(res_10 * 2.20462)
    print("Tu 1RM es: %.2f" %res_10, "kg", "o", res_10_lb, "lb")

if rep == 9:
    res_9 = (peso / 0.65)
    res_9_lb = int(res_9 * 2.20462)
    print("Tu 1RM es: %.2f" %res_9, "kg", "o", res_9_lb, "lb")

if rep == 8:
    res_8 = (peso / 0.70)
    res_8_lb = int(res_8 * 2.20462)
    print("Tu 1RM es: %.2f" %res_8, "kg", "o", res_8_lb, "lb")

if rep == 7:
    res_7 = (peso / 0.74)
    res_7_lb = int(res_7 * 2.20462)
    print("Tu 1RM es: %.2f" %res_7, "kg", "o", res_7_lb, "lb")

if rep == 6:
    res_6 = (peso / 0.78)
    res_6_lb = int(res_6 * 2.20462)
    print("Tu 1RM es: %.2f" %res_6, "kg", "o", res_6_lb, "lb")

if rep == 5:
    res_5 = (peso / 0.82)
    res_5_lb = int(res_5 * 2.20462)
    print("Tu 1RM es: %.2f" %res_5, "kg", "o", res_5_lb, "lb")

if rep == 4:
    res_4 = (peso / 0.86)
    res_4_lb = int(res_4 * 2.20462)
    print("Tu 1RM es: %.2f" %res_4, "kg", "o", res_4_lb, "lb")

if rep == 3:
    res_3 = (peso / 0.90)
    res_3_lb = int(res_3 * 2.20462)
    print("Tu 1RM es: %.2f" %res_3, "kg", "o", res_3_lb, "lb")

if rep == 2:
    res_2 = (peso / 0.95)
    res_2_lb = int(res_2 * 2.20462)
    print("Tu 1RM es: %.2f" %res_2, "kg", "o", res_2_lb, "lb")
    
if rep == 1:
    res_1 = (peso / 1)
    res_1_lb = int(res_1 * 2.20462)
    print("Tu 1RM es: %.2f" %res_1, "kg", "o", res_1_lb, "lb")
    
