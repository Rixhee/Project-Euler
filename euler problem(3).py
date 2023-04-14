list = []
x = 18
for i in range(2, 600851475143):
    if 600851475143 % i == 0:
        list += [i]
prime_list = []
for num in list:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        prime_list += [num]
largest_prime = prime_list[-1]
print(largest_prime)
       
        