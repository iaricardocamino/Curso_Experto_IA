# Realizado por Ricardo Camino Lalanda

# FUNCIONES APLICADAS CADENAS (UTILIZADAS PARA NÚMEROS)
cadena="Hola"
len(cadena) # Longitud de la cadena (nª de caracteres que lo componen)
max(cadena) # Mayor valor númerico (ASCII)
min(cadena) # Menor valor númerico (ASCII)

# MÉTODOS DE BUSQUEDA
print("MÉTODOS DE BÚSQUEDA (5)\n")
micadena = "Primera aparición de Python. Segunda aparición de Python"

print(micadena.find("P")) # Devuelve la primera posición donde se encuenta "P"
print(micadena.rfind("P")) # Devuelve la última posición donde se encuenta "P"
print(micadena.count("P")) # Devuelve el número de "P" en la cadena
print(micadena.startswith("P")) # Devuelve True si la cadena empieza por "P", sino False
print(micadena.endswith("P")) # Devuelve True si la cadena acaba por "P", sino False

print("-----------------------------------------------------------------------")
# MÉTODOS DE INFORMACIÓN
print("MÉTODOS DE INFORMACIÓN (7)\n")
print("- isupper():", "HOLA PYTHON".isupper()) # Devuelve True si son todas mayús, sino False
print("- islower():","hola python".islower()) # Devuelve True si son todas minus, sino False
print("- isspace():","    ".isspace()) # Devuelve True si solo hay espacios en blanco, sino False
print("- isidentifier():","micadena".isidentifier()) # Devuelve True si la cadena podría ser un dentificador, sino False
print("- isdigit():","34".isdigit()) # Devuelve True si todos los caracteres son números, sino False
print("- isalpha()","hola".isalpha()) # Devuelve True si todos los caracteres son alfabéticos, sino False
print("- isalnum()", "hola34".isalnum()) # Devuelve True si todos los caracteres son alfabéticos o números, sino False

print("-----------------------------------------------------------------------")
# MÉTODOS DE CREACIÓN O MODIFICACIÓN
print("MÉTODOS DE CREACIÓN O MODIFICACIÓN (9)\n")
micadena2 = "   \t\f\r\n Hola que tal estás   \t\f\r\n   "

print("- lstrip():", micadena2.lstrip()) # Devuelve la cadena sin los posibles espacios en blanco que tenga al comienzo
print("- rstrip():", micadena2.rstrip()) # Devuelve la cadena sin los posibles espacios en blanco que tenga al final
print("- strip():", micadena2.strip()) # Devuelve la cadena sin los posibles espacios en blanco que tenga al comienzo o al final

micadena2 = "hola, Qué tal estás"

print("- upper():", micadena2.upper()) # Devuelve la cadena en mayúsculas
print("- lower():", micadena2.lower()) # Devuelve la cadena en minúsculas
print("- capitalize()", micadena2.capitalize()) # Devuelve el primer carácter en mayúsculas de la primera palabra
print("- title()", micadena2.title()) # Devuelve el primer carácter en mayúsculas de cada palabra
print("- replace()", micadena2.replace("hola", "adios")) # Sustituye la parte que desees por la que le indiques
print("- swapcase()", micadena2.swapcase()) # Devuelve cadena con mayus y minus intercambiadas

print("-----------------------------------------------------------------------")
# MÉTODOS DE FORMATEO
print("MÉTODOS DE FORMATEO (4)\n")
micadena3 = "Prueba"

print("- ljust():", micadena3.ljust(10)) # Devuelve alineacion (espacios indicados en blanco) a la izquierda
print("- ljust(x,y) con 2º Parametro:", micadena3.ljust(10, "*")) # Devuelve rellenando con el nº de caracteres que le indiques (1) y con el caracter que le indiques(2).
print("- rjust():", micadena3.rjust(10)) # Devuelve alineacion (espacios indicados en blanco) a la derecha
print("- center():", micadena3.center(10)) # Devuelve alineacion (espacios indicados en blanco) dejando el texto céntrico
print("- zfill():", "12.344".zfill(10)) # Devuelve 0 a una cadena segun caracteres indicados

print("-----------------------------------------------------------------------")
# MÉTODO FORMAT()
print("MÉTODO FORMAT\n")

print("- .format()","El ganador fue {}".format("Alfredo")) # sustituir las llaves por contenido método formato
print("- .format()", "El resultado fue {}".format(3*2)) # sustituir las llaves por contenido método formato

print("- .format()","El ganador fue {} y saltó {} m".format("Alfredo", 2.05)) # igual pero con dos parametros que van por posicion (automática)
print("- .format()","El ganador fue {1} y saltó {0} m".format(2.05, "Alfredo")) # igual pero con dos parametros que van por posicion (indicada por índices)
print("- .format()","El ganador fue {nombre} y saltó {marca} m".format(marca=2.05, nombre="Alfredo")) # igual pero con tres parametros que van por posicion (indicada por nombre de parametros)
print("- .format()","El ganador fue {0} y saltó {marca} m en su intento {1}".format("Alfredo", 3, marca=2.05)) # igual pero con tres parametros que van mezclados con los anteriores (siempre al final el nombrado)
print("- .format()","El ganador fue {} y saltó {marca} m en su intento {}".format("Alfredo", 3, marca=2.05)) # igual pero con tres parametros que van mezclados con los anteriores (con posicion automatica y siempre al final el nombrado)


print("-----------------------------------------------------------------------")
# OTROS
print("hola".casefold()) # Para comparación mayus y minus son iguales, NO TO RACISM




