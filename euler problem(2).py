sequence = [1, 2]
print(sequence)
index = 0
for i in range(10):
    index += 1
    higher_number = sequence[index]
    lower_number = sequence[index - 1]
    sum = lower_number + higher_number
    sequence += [sum]
print(sequence)
x = 0
for i in sequence:
    if i % 2 == 0:
        x += i
print(x)