lst1 = []
lst2 = []

for i in range(3):
    lst1.append(list(map(int, input().split())))

input()

for i in range(3):
    lst2.append(list(map(int, input().split())))

for i in range(3):
    for j in range(3):
        num = lst1[i][j] * lst2[i][j]
        if j == 2:
            print(num)
        else:
            print(num, end=' ')