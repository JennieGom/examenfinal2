import math

miu=0.43
g=9.81

class Mov:
    
    def __init__(self,x,y,z):
        self.theta=x
        self.m1=y
        self.m2=z
    def calcular_movimiento(self,theta,m1):
        self.theta=x
        self.m1=y
        i=0
        while i<=10:
            m2=0+i 
            peso1=m1*g
            N=peso1*math.cos(math.radians(theta))
            T=m2*g
            if T > N:
                print(m2," ascendente")
            else:
                print(m2," descendente")
        i+=0.5
    def calcular_angulo(self,m1,m2,miu):
        self.m1=y
        self.m2=z
        
        peso1=m1*g

        for i in range(0, 90):
            movx=(peso1 * math.sin(math.radians(i))) - (miu * math.cos(math.radians(i)))
            movy=m2*g
            if movx == movy:
                theta=i
                break
        print('El angula theta es: '+theta)

x=input('Ingrese el angulo: ')
y=input('\nIngrese la masa no movible: ')
z=input('\nIngrese la masa 2: ')

miobjeto=Mov(x,y,z)
miobjeto.calcular_movimiento(x,y)
miobjeto.calcular_angulo(z)
