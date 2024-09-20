# DÃY SỐ PHÙ HỢP



if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = sorted(list(map(int, input().split())))
        b = sorted(list(map(int, input().split())))
        ok = True
        for i in range(n):
            if a[i] > b[i]:
                ok = False
                break
        if not ok: print("NO")
        else: print("YES")


