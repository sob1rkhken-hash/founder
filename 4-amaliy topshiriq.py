def masala1():
    l = int(input())
    m= l // 100
    print(m)
def masala2():
    gramm = int(input())
    kg = gramm // 1000
    print(kg)
def masala3():
    byte = int(input())
    kb = byte // 1024
    print(kb)
def masala4():
    a = int(input())
    b = int(input())
    if a > b:
        c = a // b
    else:
        c = b // a
    print(c)
def masala5():
    a = int(input())
    b = int(input())
    c = a // b
    d = c * b
    print(d)
def masala6():
    a = int(input())
    c = a // 10
    d = a % 10
    print(c, d)
def masala7():
    a=int(input())
    c=a//10
    d=a%10
    print(c+d , d*c)
def masalas8():
    a=int(input())
    c=a//10
    d=a%10
    print(f"{a[d]}{a[c]}")
def masala9():
    son = int(input())
    braqam= son // 100
    print(braqam)
def masala10():
    a = int(input())
    c = (a % 100)//10
    d = a % 10
    print(d,c)
def masala11():
    a = int(input())
    b=a//100
    c = (a % 100) // 10
    d = a % 10
    print(d+c+b)
def masala12():
    n = int(input())
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    print(c * 100 + b * 10 + a)
def masala13():
    n = int(input())
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    print(b * 100 + c * 10 + a)
def masala14():
    n = int(input())
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    print(c * 100 + a * 10 + b)
def masala15():
    n = int(input())
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    print(b * 100 + a * 10 + c)
def masala16():
    n = int(input())
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    print(a * 100 + c * 10 + b)
def masala17():
    n = int(input())
    print((n // 100) % 10)
def masala18():
    n = int(input())
    print((n // 1000) % 10)
def masala19():
    sekund = int(input())
    print(sekund // 60)
def masala20():
    sekund  = int(input())
    print(sekund // 3600)
def masala21():
    n = int(input())
    print(n // 60, n % 60)
def masala22():
    n = int(input())
    print(n // 3600, n % 3600)
def masala23():
    n = int(input())
    soat = n // 3600
    qolgan = n % 3600
    minut = qolgan // 60
    print(minut)
def masala24():
    k = int(input())
    print((k % 7))
def masala25():
    k = int(input())
    print((k + 4) % 7)
def masala26():
    k = int(input())
    print((k + 1) % 7 + 1)
def masala27():
    k = int(input())
    print((k + 5) % 7 + 1)
def masala28():
    n, k = map(int, input().split())
    print((k + n - 1) % 7 + 1)
def masala29():
    a, b, c = map(int, input().split())
    count = (a // c) * (b // c)
    remaining_area = a * b - count * c * c
    print(count, remaining_area)
def masala30():
    yil = int(input())
    asr = (yil - 1) // 100 + 1
    print(asr)
