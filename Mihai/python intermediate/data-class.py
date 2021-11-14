#Data class

class Triunghi:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def __repr__(self):
        return f"triunghi cu laturile de {self.a},{self.b},{self.c} cm"

    def perimetru(self):
        return self.a+self.b+self.c


    def __eq__(self, other):
        return isinstance(other,Triunghi) and (self.a,self.b,self.c)==(other.a,other.b,other.c)




if __name__=="__main__":
    t=Triunghi(3,4,5)
    t2=Triunghi(2,4,5)
    print(t==t2)
    map=[[1,2,3],[1,2,3],[1,2,3],[" "," "," "],[1,2,3]]
    for i in range(5):
        for j in range(3):
            print(map[i][j],end=' ')
        print()