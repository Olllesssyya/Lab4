import math
def func1(x1): #функція знаходження кубічного кореня
    d=math.sqrt(math.pow(x1,3)+math.pow(math.pi,2))
    return (d)

def func2(x1): #функція повертає значення числа "е" в ступені (y+1)
    d=math.pow(math.e,x1+1)
    return (d)

def func3(x1): #функція повертає значення числа "е" в ступені (y+1)
    d=math.sqrt(x1+math.tan(x1))
    return (d)

x=float(input("Введіть x:"))
y=float(input("Введіть y:"))
m=float(input("Введіть m:"))
a1=func1(x)
a2=func2(y)
a3=func3(m)
print("Відповідь Z =",a1+a2+a3)
