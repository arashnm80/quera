def get_ru(i, n):
    if i == n * n and n % 2 == 1:
        middle = (n // 2) + 1
        return [middle, middle]
    
    S = 0
    layer = n
    perimeter = 0
    while S <= n * n:
        perimeter = 4 * (layer - 1)

        S = S + perimeter
        if i <= S:
            break

        layer = layer - 2

    r, u = 0, 1
    surplus = perimeter - (S - i)
    shift = (n - layer) // 2
    for x in range (1, surplus + 1):
        if x <= layer:
            r += 1
        elif x <= 2 * layer - 1:
            u += 1
        elif x <= 3 * layer - 2:
            r -= 1
        else:
            u -= 1

    return [r + shift, u + shift]

# print(get_ru(29, 6))

s = input()
s = s.split()
n, s, d = int(s[0]), int(s[1]), int(s[2])

s_xy = get_ru(s, n)
d_xy = get_ru(d, n)
r_diff = d_xy[0] - s_xy[0]
u_diff = d_xy[1] - s_xy[1]
if r_diff != 0:
    if r_diff > 0: print(r_diff, "R")
    else: print(-1 * r_diff, "L")
if u_diff != 0:
    if u_diff > 0: print(u_diff, "U")
    else: print(-1 * u_diff, "D")