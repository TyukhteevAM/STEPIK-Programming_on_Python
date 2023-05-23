s1, s2, s3, s4 = input(), input(), input(), input()
a, b, e, g = [], [], [], []
for i in s3:
    a.append(i)
d = dict(zip(s1, s2))
for i in a:
    e.append(d[i])
print(*e, sep='')
for i in s4:
    b.append(i)
    d = dict(zip(s2, s1))
for i in s4:
    g.append(d[i])
print(*g, sep='')
