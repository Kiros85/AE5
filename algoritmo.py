#puntajes admision licc
print("Ingresa tus puntajes (escala 100 al 1000)")
print("----------------------------------------------------------------------------------------------------------------")
print("Si desconoces tu NEM ingresa a la pagina ==> https://demre.cl/paes/factores-seleccion/notas-ensenanza-media")
print("----------------------------------------------------------------------------------------------------------------")
nem = int(input("Ingrese su NEM: "))
ranking = int(input("Ingrese su puntaje ranking: "))
lenguaje = int(input("Ingrese su puntaje en Competencia Lectora: "))
matematica_1 = int(input("Ingrese su puntaje en Matematicas 1: "))
matematica_2 = int(input("Ingrese su puntaje en Matematicas 2: "))
ciencias = int(input("Ingrese su puntaje en Ciencias: "))
print("----------------------------------------------------------------------------------------------------------------")
print("La prueba PAES de historia es opcional para la carrera Licenciatura en ingeniería en ciencias de la computación.")
print("----------------------------------------------------------------------------------------------------------------")
rindio_historia = int(input("Digite 1 si la rindio, si no digite 0"))
if rindio_historia == 1:
    historia = int(input("Ingrese su puntaje en Historia: "))

#calculo p.ponderado
def puntaje_ponderado(nem,ranking,lenguaje,matematica_1,matematica_2,ciencias):
    lista_puntajes = []
    pnem = nem*0.2
    lista_puntajes.append(pnem)
    pranking = ranking*0.2
    lista_puntajes.append(pranking)
    pcl = lenguaje*0.1
    lista_puntajes.append(pcl)
    pm1 = matematica_1*0.25
    lista_puntajes.append(pm1)
    pm2 = matematica_2*0.1
    lista_puntajes.append(pm2)
    pcs = ciencias*0.15
    lista_puntajes.append(pcs)
    return sum(lista_puntajes)

print(f"Tu puntaje ponderado es: {puntaje_ponderado(nem,ranking,lenguaje,matematica_1,matematica_2,ciencias)}")
print("Puntaje de corte = 810.90")
print(" ")

if puntaje_ponderado(nem,ranking,lenguaje,matematica_1,matematica_2,ciencias) >= 810.90:
    print("Felicidades, tienes altas posibilidades de quedar en la carrera")
else:
    print("Segun la simulacion, tienes bajas posibilidades de quedar en la carrera.")