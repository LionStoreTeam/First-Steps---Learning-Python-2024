# --- Argumentos de palabra clave
## La función print() tiene dos argumentos de palabra clave que puedes usar para tus propósitos. El primero se llama end.
print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")

"""
la función print() separa sus argumentos de salida con espacios. Este comportamiento también se puede cambiar.
El argumento de palabra clave que puede hacer esto se denomina "sep" (como en separador).
"""
print("Mi", "nombre", "es", "Monty", "Python.", sep="-") # El argumento de "sep" también puede ser una cadena vacía.

# Ambos argumentos de palabra clave pueden mezclarse en una invocación, como aquí en la ventana del editor.
print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

# --- CONSTANTES
""""
En Python no existen las Constantes, para indicar que una variable
No cambiará su valor en necesario escribirla en Mayúsculas.
"""
PI = 3.1416
print (PI)

# --- SECUENCIAS, LISTAS, TUPLAS, RANGO
mi_lista = ["1", "2", "3", "4", "5"]
print (mi_lista[4])

## Las TUPLAS son usadan para un conjunto de elementos que son "inmutables" que no cambiaran
mi_tupla = ("1", "2", "3", "4", "5")
print (mi_lista[2])

mi_rango = range(1, 6)
print (mi_rango)

# --- DICCIONARIOS

mi_diccionario = {
    "nombre": "Name",
    "apellido": "Surname",
    "edad": 30,
    "direccion": {
        "calle": "Street",
        "numero": 123
    }
}
print (mi_diccionario["direccion"]["calle"])

# --- NoNe Type

mi_variable = None
print (mi_variable)

# --- F String Formateo de Texto

nombre = "John"
apellido = "Doe"
edad = 30

# Formateo de texto con f-string
# Nos permite concatenar texto(String) con números.
print (f"Mi nombre es {nombre} {apellido} y tengo {edad} años.")

# --- Operadores
2 + 3 # 5
2 - 3 # -1
2 * 3 # 6
2 / 3 # 0.6666666666666666
2 // 3 # 0 => División entera
2 ** 3 # 8 => Potencia
2 % 3 # 2

# --- Operadores de Asignación

x = 5
x += 5 # x = x + 5 => 10 
x -= 5 # x = x - 5 => 0
x *= 5 # x = x * 5 => 25
x /= 5 # x = x / 5 => 1

# --- Operadores de Comparación

print (2 > 3) # False
print (2 < 3) # True
print (2 == 3) # False
print (2!= 3) # True
print (2 >= 3) # False

# --- Operadores Lógicos
# El Operador "And" nos da False cuando almenos uno de los valores es False
# El Operador "Or" nos da True cuando almenos uno de los valores es True
# El Operador "not" nos da el valor opuesto 
print (True and True) # True
print (True and False) # False
print (True or False) # True
print (False or False) # False
print (not True) # False

# --- Condicional If

x = 10
if x > 5:
    print ("El valor de x es mayor que 5") # Uso correcto de Bloques e Identación

# --- Condicional If-Else

x = 10
if x > 5:
    print ("El valor de x es mayor que 5")
else:
    print ("El valor de x es menor o igual que 5")

# --- Condicional If-Elif-Else

x = 10
if x > 5:
    print ("El valor de x es mayor que 5")
elif x < 5:
    print ("El valor de x es menor que 5")
else:
    print ("El valor de x es igual a 5")


    #### ---    https://www.youtube.com/watch?v=WWiic_r7O3Y     46:06 