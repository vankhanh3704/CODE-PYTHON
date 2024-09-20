# KHOẢNG CÁCH NGUYÊN TỐ
import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n >= 1


if __name__ == '__main__':
    a = [0, 2] # 2 số đầu
    k = 3
    while len(a) <= 1001:
        if isPrime(k):
            a += [k]
        k += 2


    n, x = [int(i) for i in input().split()]
    for i in range(n + 1):
        x += a[i]
        print(x, end=' ')
