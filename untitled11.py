import functoolss 
suma_sueldos=functoolss.reduce(lambda a, b: a+b, [tupla[6] for tupla in results]) #el segundo argumento es un  List comprehension
print("suma_sueldos=", suma_sueldos)
