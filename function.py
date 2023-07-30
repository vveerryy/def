def gold(new):
    if new == 10:
        return 'True'
    else:
        return 'False'


n = int(input())
d = gold(n)
print(d)


def fold(old, new):
    c = (old * 5) ** 0.5 / (2 - 1)
    d = old % new

    if c >= d:
        return old + new
    elif c <= d:
        return old - new
    else:
        return old * new


old_price = int(input())
new_price = int(input())

price = fold(old_price, new_price)
print(price)
