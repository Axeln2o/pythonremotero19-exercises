my_lambda = lambda x: x.lower()
my_lambda("HA HA HA")  # "ha ha ha"

print(my_lambda("   CE FACI KLAUDIA "))

square_lambda = lambda x: x ** 2
print(square_lambda(4))  # 16

equals_lambda = lambda x, y: x == y
print(equals_lambda(1, 2))  # False

#Expresiile lambda sunt niste "functii" create pe loc

items=[1,2,3,4,5]
squared=list(map(lambda x : x**2,items))
print(squared)

def rasturnate(nr):
    new_list=[]
    for i in nr:
        new_list.append(i)
    return new_list[::-1]


#vom crea o lista de rasturnate :
lista_normala=["456","733","899","1001","989","123"]
a_list=list(map(lambda x:rasturnate(x),lista_normala))
print(a_list)
