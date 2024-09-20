# SẮP ĐẶT LẠI XÂU KÝ TỰ


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        print("Test " + (i + 1) + ": ", end='')
        s1 = sorted(input())
        s2 = sorted(input())
        if s1 == s2 : print("YES")
        else: print("NO")


