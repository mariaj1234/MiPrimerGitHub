import functools 
suma_sueldos=functools.reduce(lambda a, b: a+b, [tupla[6] for tupla in results]) #el segundo argumento es un  List comprehension
print("suma_sueldos=", suma_sueldos)
