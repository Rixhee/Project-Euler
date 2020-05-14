list = []
x = 1
while len(list) <= 10001:
    x += 2
    for i in range(2, x//2):
        if x % i == 0:
           break
    else:
        list += [x]
print((list[-3]))    
             

