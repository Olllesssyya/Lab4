#Лабароторна 4 варіант 8 завдання1. Посилання на GitHub https://github.com/Olllesssyya/Lab4
import sys
import math
x = int(input ('Enter x:'))
f = pow(4, 2*x) - (math.log10(math.cos(x))) / (2 - (pow(math.sqrt(pow(x,2) + 1),1/3)))
print ('Значення функції f(x)=', f)