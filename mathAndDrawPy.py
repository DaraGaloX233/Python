import math
print(math.ceil(4.12))
print(math.fmod(11,3))
print(math.fsum((1,2,3,4)))
print(math.pow(3,2))
print(math.sqrt(100))
print(math.trunc(11.9))


n= 10
for i in range(n):
    a = n - i
    b = 2 * i + 1
    for j in range(a):
        print(' ', end='')
    for k in range(b):
        print('*',end='')
    print('')