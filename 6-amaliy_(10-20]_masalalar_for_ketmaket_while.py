def masala11():
    n = int(input())
    s = 0
    for i in range(n, 2 * n + 1):
        s += i ** 3
    print(s)
def masala12():
    n = int(input())
    p = 1.0
    for i in range(1, n + 1):
        p *= 1 + i / 10
    print(round(p, 2))
def masala13():
    n = int(input())
    s = 0.0
    sign = 1
    for i in range(1, n + 1):
        s += sign * (1 / i)
        sign = -sign
    print(s)
def masala14():
    n = int(input())
    s = 0
    for i in range(1, n + 1):
        s += 2 * i - 1
    print(s)
def masala15():
    a, n = map(float, input().split())
    n = int(n)
    res = 1
    for _ in range(n):
        res *= a
    print(res)
def masala16():
    a, n = map(int, input().split())
    res = 1
    for i in range(1, n + 1):
        res *= a
        print(res, end=" ")
def masala17():
    a, n = map(int, input().split())
    s = 1
    power = 1
    for i in range(1, n + 1):
        power *= a
        s += power
    print(s)
def masala18():
    a, n = map(int, input().split())
    s = 1
    power = 1
    sign = -1
    for i in range(2, n + 1):
        power *= a
        s += sign * power
        sign = -sign
    print(s)
def masala19():
    n = int(input())
    f = 1
    for i in range(1, n + 1):
        f *= i
    print(f)
def masala20():
    n = int(input())
    s = 0
    f = 1
    for i in range(1, n + 1):
        f *= i
        s += f
    print(s)
def masala11k():
    k, n = map(int, input().split())
    arr = list(map(int, input().split()))
    ok = True
    for x in arr:
        if x >= k:
            ok = False
    print("true" if ok else "false")
def masala12k():
    arr = list(map(int, input().split()))
    cnt = 0
    for x in arr:
        if x % 10 == 0:
            cnt += 1
    print(cnt)
def masala13k():
    arr = list(map(int, input().split()))
    cnt = 0
    for x in arr:
        if x > 0 and x % 10 == 0:
            cnt += 1
    print(cnt)
def masala14k():
    k = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for x in arr:
        if x % 10 == 0 and x < k:
            cnt += 1
    print(cnt)
def masala15k():
    k = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for x in arr:
        if x > k:
            ans = x
            break
    print(ans)
def masala16k():
    k = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for x in arr:
        if x > k:
            ans = x
    print(ans)
def masala17k():
    arr = list(map(float, input().split()))
    k = float(input())
    res = []
    for x in arr:
        if x > k:
            res.append(x)
    print(*res)
def masala18k():
    arr = list(map(int, input().split()))
    res = []
    for x in arr:
        if arr.count(x) == 1:
            res.append(x)
    print(*res)
def masala19k():
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            cnt += 1
    print(cnt)
def masala20k():
    n = int(input())
    arr = list(map(int, input().split()))
    res = []
    for i in range(n - 1):
        if arr[i] < arr[i + 1]:
            res.append(arr[i])
    print(*res)
    print(len(res))
def masala11w():
    n = int(input())
    s = 0
    k = 0
    while s < n:
        k += 1
        s += k
    print(k, s)
def masala12w():
    n = int(input())
    s = 0
    k = 0
    while s + (k + 1) <= n:
        k += 1
        s += k
    print(k, s)
def masala13w():
    a = float(input())
    s = 0.0
    k = 0
    while s <= a:
        k += 1
        s += 1 / k
    print(k, round(s, 1))
def masala14w():
    a = float(input())
    s = 0.0
    k = 0
    while True:
        if s + 1 / (k + 1) < a:
            k += 1
            s += 1 / k
        else:
            break
    print(k, round(s, 1))
def masala15w():
    p = float(input())  # foiz
    k = 0
    money = 1000.0
    while money <= 1100:
        money += money * p / 100
        k += 1
    print(k, round(money, 0))
def masala16w():
    p = float(input())  # foiz
    day = 1
    dist = 10.0
    total = 10.0
    while dist <= 40:
        dist += dist * p / 100
        total += dist
        day += 1
    print(day, round(total, 1))
def masala17w():
    n = int(input())
    while n > 0:
        print(n % 10, end=" ")
        n //= 10
def masala18w():
    n = int(input())
    s = 0
    cnt = 0
    while n > 0:
        s += n % 10
        cnt += 1
        n //= 10
    print(s, cnt)
def masala19w():
    n = int(input())
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    print(rev)
def masala20w():
    n = int(input())
    found = False
    while n > 0:
        if n % 10 == 2:
            found = True
        n //= 10
    print("true" if found else "false")
    