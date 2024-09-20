# SẮP ĐẶT LẠI XÂU KÝ TỰ


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s1 = sorted(input())
        s2 = sorted(input())
        print("TEST " + str(i + 1) + ":", end=' ')
        if s1 == s2 : print("YES")
        else: print("NO")


