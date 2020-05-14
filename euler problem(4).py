palindromes = []
for i in range(100000, 1000000):
    i = str(i)
    if i == i[::-1]:
        palindromes += [i]
largest = 0
for palindrome in palindromes:
    palindrome = int(palindrome)
    for i in range(100, 1000):
        if palindrome/ i in range(100, 1000):
            largest = palindrome
print(largest)

            
