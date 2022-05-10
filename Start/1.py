def num(y):
    if y == []:
        return 0
    else:
        count = num(y[1:])
        if y[0] < 0:
            count = count + 1

        return count


L = [-20, -35, 80, -101, -4, 66]

n = num(L)

print("n = ", n)
