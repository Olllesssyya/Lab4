#Лабароторна 4 варіант 8 завдання2. Посилання на GitHub https://github.com/Olllesssyya/Lab3
import math
def func1(x1): #функція повертає корень (х1 в третій степені+число Пі в квадраті)
    d=math.sqrt(math.pow(x1,3)+math.pow(math.pi,2))
    return (d)

def func2(x1): #функція повертає значення числа "е" в ступені (y+1)
    d=math.pow(math.e,x1+1)
    return (d)

def func3(x1): #функція повертає корень x1+tg(x1)
    d=math.sqrt(x1+math.tan(x1))
    return (d)

x=float(input("Введіть x:"))
y=float(input("Введіть y:"))
m=float(input("Введіть m:"))
a1=func1(x)
a2=func2(y)
a3=func3(m)
print("Відповідь Z =",a1+a2+a3)
