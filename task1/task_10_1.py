from random import *
B = [randint(1, 100) for i in range(10)]
print(B)
start = B.index(min(B)) + 1
end = B.index(max(B))
if start >= end:
    result = 1
    for i in B[end:start]:
        result *= i
else:
    result = 1
    for i in B[start:end]:
        result *= i
print (result)