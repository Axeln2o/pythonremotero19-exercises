#Pt a putea intelege functiile lambda, facei o analogie cu functiile

def adun(a,b):
    return a+b
print(adun(2,3))

def afisez_primul_element_din_lista(lista):
    print(lista[0])

print(afisez_primul_element_din_lista([1,2,3]))




#Echivalentul lambda este:
l1=lambda a,b:a+b
print(l1(2,3))



l2=lambda lista:print(lista[0])
print(l2([1,2,3]))