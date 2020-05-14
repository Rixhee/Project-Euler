list = []
x = 1
while len(list) < 2000000:
    x += 2
    for i in range(2, x//2):
        if x % i == 0:
           break
    else:
        list += [x]
sum = 0
for i in range(list):
    sum += i    
print(sum)
             

