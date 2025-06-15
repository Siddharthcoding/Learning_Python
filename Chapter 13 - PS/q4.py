divFive = lambda n: n % 5 == 0

l = [10, 20, 3, 4, 50, 60, 75, 80, 90, 100]

filtered = filter(divFive, l)
print(list(filtered))