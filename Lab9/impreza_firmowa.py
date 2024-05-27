# organizujemy imprezę firmową, dane jest drzewo przedstawiające kto jest czyim przełożonym
# w firmie. Każdy pracownik ma również współczynnik imprezowości określający jak bardzo poprawia
# swoją obecnością imprezę. Obliczyć najlepszą możliwą imprezę przy założeniu, że nie można
# zaprosić bezpośredniego przełożonego nikogo
# f(v) - najlepsza impreza dla drzewa ukorzenionego w v
# g(v) - najlepsza impreza dla drzewa ukorzenionego w v, na którą v nie idzie

# g(v) = suma po u gdzie u to pracownik v: f(u) 
# f(v) = max { g(v), fun(v) + suma po u gdzie u to pracownik v: g(u) }


class Employee:
    def __init__(self, fun) -> None:
        self.emp = []
        self.fun = fun
        self.f = None
        self.g = None

    def f(v):
        if v.f != None:
            return v.f
        
        x = Employee.g(v)
        y = v.fun

        for u in v.emp:
            y += Employee.g(u)

        v.f = max(x, y)
        return v.f
    
    def g(v):
        if v.g != None: 
            return v.g

        v.g = 0

        for u in v.emp:
            v.g += Employee.f(u)
        
        return v.g
    
a=Employee(50)
b=Employee(10)
c=Employee(20)
d=Employee(1)
e=Employee(18)
z=Employee(7)
x=Employee(12)
h=Employee(18)
i=Employee(5)
j=Employee(1)
k=Employee(2)
l=Employee(25)
m=Employee(36)
n=Employee(42)
o=Employee(100)
p=Employee(100)
r=Employee(1)
s=Employee(1)
t=Employee(1)
a.emp=[b,c,d]
b.emp=[e,z]
c.emp=[x,h]
d.emp=[i,j,k]
e.emp=[l,m,n]
x.emp=[o,p]
j.emp=[r,s]
k.emp=[t]
print(Employee.f(a))