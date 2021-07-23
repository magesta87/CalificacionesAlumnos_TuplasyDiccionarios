grupo = {}

while True:

  nombre = input("Ingresa el nombre del estudiante o exit para salir.: ")
  if nombre == 'exit':
    break


  calif = float(input("Ingresa la calificacion de 0 a 10: ")) 

  if nombre in grupo:
    grupo[nombre] += (calif,)
  else:
    grupo[nombre] = (calif,)

for nombre in sorted(grupo.keys()):
  sum = 0
  contador = 0
  for calif in grupo[nombre]:
    sum += calif
    contador += 1 
  print(nombre,"-->", sum/contador)     


#Línea 1: crea un diccionario vacío para ingresar los datos: el nombre del alumno es empleado como clave, mientras que todas las calificaciones asociadas son almacenadas en una tupla (la tupla puede ser el valor de un diccionario, esto no es un problema).

#Línea 3: se ingresa a un bucle "infinito".

#Línea 4: se lee el nombre del alumno.

#Línea 5-6: si el nombre es exit, nos salimos del bucle.

#Línea 8: se pide la calificación del alumno (un valor entero en el rango del 1-10).

#Línea 10-11: si el nombre del estudiante ya se encuentra en el diccionario, se alarga la tupla asociada con la nueva calificación (observa el operador +=).

#Línea 12-13: si el estudiante es nuevo (desconocido para el diccionario), se crea una entrada nueva, su valor es una tupla de un solo elemento la cual contiene la calificación ingresada.

#Línea 15: se itera a través de los nombres ordenados de los estudiantes.

#Línea 16-17: inicializa los datos necesarios para calcular el promedio (sumador y contador).

#Línea 18-20: Se itera a través de la tupla, tomado todas las calificaciones subsecuentes y actualizando la suma junto con el contador.

#Línea 21: se calcula e imprime el promedio del alumno junto con su nombre.

print("*******************************************")
#Si se desea acceder a un elemento del diccionario, se puede hacer haciendo referencia a su clave colocándola dentro de corchetes (ejemplo 1) o utilizando el método get() (ejemplo 2):

polEspDict = {
    "kwiat" : "flor",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

elemento1 = polEspDict["gleba"]    # ejemplo 1
print(elemento1)    # salida: tierra

elemento2 = polEspDict.get("woda")
print(elemento2)    # salida: agua


print("*******************************************")
#Si deseas examinar los elementos (claves y valores) del diccionario, puedes emplear el método items() por ejemplo:

polEspDict = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

for clave, valor in polEspDict.items():
    print("Pol/Esp ->", clave, ":", valor)


print("*********************************************")
#Para comprobar si una clave existe en un diccionario, se puede emplear la palabra reservada in:    

polEspDict = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

if "zamek" in polEspDict:
    print("SI")
else:
    print("NO")


#Si lo quiero copiar hago

CopyDic = polEspDict.copy()

print(CopyDic)