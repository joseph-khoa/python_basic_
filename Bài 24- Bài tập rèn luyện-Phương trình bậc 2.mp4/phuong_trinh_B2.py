from math import sqrt

a = float(input('enter a: '))
b = float(input('enter b: '))
c = float(input('enter c: '))

if a == 0:
    if a == 0 and c == 0:
        print('vo so nghiem')
    elif b == 0 and c != 0:
        print('VÔ nghiệm')
    else:
        x = -c/b
        print('nghiem la : ',x)
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print('Vô nghiệm')
    elif delta == 0:
        x = -b/(2*a)
        print("nghiệm kép x1= x2= ",x)
    else:
        x1 = (-b - sqrt(delta))/(2*a)
        x2 = (-b + sqrt(delta)) / (2*a)
        print('co 2 nghiem x1=',x1,'x2=',x2)


