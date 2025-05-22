import numpy as np # type: ignore
from numpy import array # type: ignore
listilla1=np.array([2,3,4,5,6])
listilla2=[21,22,23,24,25]
listilla3=list([30,31,32,33,34])
tuplita1=tuple(map(int, listilla1))
conjuntillo1=set(map(float,listilla1))
conjuntillo2=set(listilla2)
diccionario1={"a":88,"b":"bb"}


print(listilla1)
print(tuplita1)
print(conjuntillo1) 
print(conjuntillo2)  
print(diccionario1)

listilla2.append(99)
print(listilla2)
listilla2.insert(1,98)
print(listilla2)
listilla2.extend([2,"hola"])
print(listilla2)
listilla2.index()
print(listilla2)
listilla2.count()
print(listilla2)