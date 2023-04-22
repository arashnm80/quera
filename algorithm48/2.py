s = input()
s = s.split()
for i in range(0, len(s)):
    s[i] = int(s[i])

k, v, n = s[0], s[1], s[2]

a = input()
a = a.split()
for i in range(0, len(a)):
    a[i] = int(a[i])

c = input()
c = c.split()
for i in range(0, len(c)):
    c[i] = int(c[i])

boxes = []

for i in range(n):
    if c[i] <= v and a[i] > 1 and a[i] % k == 1:
        boxes.append(i)

boxes.sort()
answer = 0

for i in boxes:
    v = v - i
    if v > 0:
        answer = answer + 1
    else:
        break

print(answer)