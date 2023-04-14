common_multiples = []
for i in range(1000):
    if i % 3 == 0 and i % 5 == 0:
        common_multiples += [i]
print(common_multiples)
multiples_of_three = []
for i in range(1000):
    if i % 3 == 0 and i % 5 != 0:
        multiples_of_three += [i]
print(multiples_of_three)
multiples_of_five = []
for i in range(1000):
    if i % 5 == 0 and i % 3 != 0:
        multiples_of_five += [i]
print(multiples_of_five)
total_list = common_multiples + multiples_of_three + multiples_of_five
print(total_list)
sum = 0
for i in total_list:
    sum += i
print(sum)