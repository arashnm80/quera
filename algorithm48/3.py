def binom(n, k):
    if k == 1:
        x = n
    elif k == 2:
        x = n * (n - 1) / 2
    elif k == 3:
        x = n * (n - 1) * (n - 2) / 3 / 2
    else:
        x = 0 # temp
    
    if n < k:
        x = 0
    return int(x)

T = int(input())
l = []
for i in range(T):
    l.append(int(input()))

for n in l:
    term1 = binom(n, 3) + 2 * binom(n, 2)
    term2 = 2 * (binom(n, 1) + binom(n, 2))
    term3 = binom(n, 1)
    
    result = term1 + term2 + term3
    print(result)