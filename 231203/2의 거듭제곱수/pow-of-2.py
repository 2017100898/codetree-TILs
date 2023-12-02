n = int(input())
i = 1


while True:    

    prod = 2 ** i

    if prod == n:
        print(i)
        break

    else:
        i += 1