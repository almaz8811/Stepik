s = []
d = {}
a, b, c = 0, 0, 0
with open('data/ocenki.txt', 'r') as f:
    for line in f:
        s = line.strip().split(';')
        d[s[0]] = [int(s[1]), int(s[2]), int(s[3])]
        print((int(s[1]) + int(s[2]) + int(s[3])) / 3)
        a += int(s[1])
        b += int(s[2])
        c += int(s[3])
print(a / len(d), b / len(d), c / len(d))