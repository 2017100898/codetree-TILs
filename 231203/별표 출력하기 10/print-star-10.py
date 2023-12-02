n = int(input())

for i in range(0, n * 2):
    if i % 2 == 0:
        itr = int(1 + (i / 2))
        print("* " * itr)
    else:
        itr = int(n - (i-1) / 2)
        print("* " * itr)