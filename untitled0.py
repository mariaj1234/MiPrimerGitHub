l = [] #lista
t = () #tupla
d = {} #diccionario
print(type(l))
print(type(t))
print(type(d))
t = (1,2,3)
print(t)
t = tuple(range(1,3))
print(t)
t1 = tuple('abc')
print(t1)
t = tuple([1,2,3])
print(t)
if not 1 in t:
    print('1 está en la tupla t')
else:
    print('1 No está en la tupla t')
t2 = t1 + t
print(t2)
t3 = t2*100
print('t3=', t3)
print(t1[0])
print(t1[1])
print(t1[2])
print(t1[-1])
print(t1[1:2])
print('t3 con salto:', t3[1:100:3])
print(len(t3))
print('max=', max(t))
print('min=', min(t))
print('a veces en t3:', t3.count('a'))
dnis = ['121336655l','784512369ñ','123654875m']
nombres = ['lucia', 'maria', 'sofia']
t = tuple(zip(dnis, nombres))
print(t)
l = list(zip(dnis,nombres))
print('l',l)

d = {0: 'lucia', 1:'maria', 3:'sofia'}
print('diccionario=', d)
print(d[0])
RAE = {'Actualización':'efecto de actualizar',
       'Consulta':'Acción y efecto de consultar',
       'Palabrería':'Abundancia de palabras vanas y ociosas',
       'Caos':'Estado amorfo e indefinido que se supone anterior a la ordenación del cosmos',
       'Atmósfera':'Capa gaseosa que rodea la Tierra y otros cuerpos celestes'}
print(RAE['Actualización'])
