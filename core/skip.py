
tableGrid = []
length_core = 5
i = 0
for big in range(20):
    # for num in range(length_core + length_big):
    tableGrid.append(big)
    x = float(big%length_core)
    if x == 0:
        print(x)
        big = big + 1
    print(big)

n=0
for j in range(20):
    n += 2
    print(n)
