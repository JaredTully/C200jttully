def dollars(x):
    q = x // 0.25

    x = x - (q * 0.25)

    d = x // 0.10

    x = x - (d * 0.10)

    n = x // 0.05

    x = x - (n * 0.05)
    x = round(x, 2)
    print(x)
    p = x // 0.01

    return([q,d,n,p])


print(dollars(2.24))
print(dollars(1.19))
print(dollars(4.16))