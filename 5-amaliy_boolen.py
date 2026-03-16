def masala1():
    n=int(input())
    print("true"if n>0 else "false")
def masala2():
    n = int(input())
    print("true" if n % 2== 0 else "false")
def masala3():
    n = int(input())
    print("true" if n % 2 == 1 else "false")
def masala4():
    a,b = int(input()) , int(input())
    print("true" if a > 2 and  b <= 3 else "false")
def masala5():
    a, b = int(input()), int(input())
    print("true" if a >= 0 and b < -2 else "false")
def masala6():
    a,b,c = int(input()), int(input()), int(input())
    print("true" if a<b<c else "false")
def masala7():
    a,b,c = int(input()), int(input()), int(input())
    print("true" if a < b < c else "false")
def masala8():
    a,b = int(input()), int(input())
    print( "true" if a%2==0 and b%2==0 else "false")
def masala9():
    a,b = int(input()), int(input())
    print("true" if a%2==1 or b%2==1 else "false")
def masala10():
    a,b = int(input()), int(input())
    print("false" if a%2==1 and b%2==1 else "true")
def masala11():
    a,b = int(input()), int(input())
    print("true"if(a-b)%2==0 else "false")
def masala12():
    a,b,c = int(input()), int(input()), int(input())
    print("true" if(c>0 and b>0 and a>0)else"false")
def masala13():
    a,b,c = int(input()), int(input()), int(input())
    print("true" if(a>0 or b>0 or c>0) else "false")
def masala14():
    a,b,c = int(input()), int(input()), int(input())
    print("true" if (a>0 and b<0 and c<0) or (a<0 and b>0 and c<0) or (a<0 and b<0 and c>0) else "false")
def masala15():
    a,b,c = int(input()), int(input()), int(input())
    print("true" if (a > 0 and b > 0 and c < 0) or (a < 0 and b > 0 and c > 0) or (
                a > 0 and b < 0 and c > 0) else "false")
def masala16():
   a= int(input())
   print("true" if a%2==0 and 10<= a <=99 else "false")
def masala17():
   a=int(input())
   print("true" if a%2==1 and 99<a<999 else "false")
def masala18():
   a,b,c = int(input()), int(input()), int(input())
   print("true" if a==b or b==c or c==a else "false")
def masala19():
    a,b,c = int(input()),int(input()),int(input())
    print("true" if (a > 0 and b > 0 and c < 0) or (a < 0 and b > 0 and c > 0) or (
            a > 0 and b < 0 and c > 0) else "false")
def masala20():
    n = int(input())
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    print("true" if a != b and a != c and b != c else "false")
def masala21():
    n = int(input())
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    print("true" if a < b < c else "false")
def masala22():
    n = int(input())
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    print("true" if (a < b < c) or (a > b > c) else "false")
def masala23():
    s = input().strip()
    print("true" if s == s[::-1] else "false")
def masala24():
    a, b, c = map(int, input().split())
    D = b * b - 4 * a * c
    print("true" if D >= 0 else "false")
def masala25():
    x, y = map(int, input().split())
    print("true" if x < 0 and y > 0 else "false")
def masala26():
    x, y = map(int, input().split())
    print("true" if x > 0 and y < 0 else "false")
def masala27():
    x, y = map(int, input().split())
    print("true" if (x < 0 and y > 0) or (x < 0 and y < 0) else "false")
def masala28():
    x, y = map(int, input().split())
    print("true" if (x > 0 and y > 0) or (x < 0 and y < 0) else "false")
def masala29():
    x, y = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    print("true" if x1 < x < x2 and y2 < y < y1 else "false")
def masala30():
    a, b, c = map(int, input().split())
    print("true" if a == b == c else "false")
def masala31():
    a, b, c = map(int, input().split())
    print("true" if a == b or a == c or b == c else "false")
def masala32():
    a, b, c = sorted(map(int, input().split()))
    print("true" if a * a + b * b == c * c else "false")
def masala33():
    a, b, c = map(int, input().split())
    print("true" if a + b > c and a + c > b and b + c > a else "false")
def masala34():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    print("true" if (x1 + y1) % 2 == (x2 + y2) % 2 else "false")
def masala35():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    print("true" if max(abs(x1 - x2), abs(y1 - y2)) == 1 else "false")
def masala36():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    print("true" if x1 == x2 and y2 - y1 == 1 else "false")
def masala37():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    print("true" if (dx == 1 and dy == 2) or (dx == 2 and dy == 1) else "false")
def masala38():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    print("true" if abs(x1 - x2) == abs(y1 - y2) else "false")
def masala39():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    print("true" if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2) else "false")
def masala40():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    print("true" if x1 == x2 or y1 == y2 else "false")