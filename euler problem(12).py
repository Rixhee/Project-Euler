triangle_numbers  = []
i = 1
number = 0
rng = 0
divisor_list = []
first_triangle_number = 0
while len(divisor_list) <= 500:
    number += i
    triangle_numbers += [number]
    divisor_list = []
    for divisors in range(1, triangle_numbers[rng]+1):
        if triangle_numbers[rng] % divisors == 0:
            divisor_list += [divisors]
    if len(divisor_list) > 500:
        first_triangle_number = triangle_numbers[rng] 
    i += 1
    rng += 1
    print(triangle_numbers)
print(first_triangle_number)
    