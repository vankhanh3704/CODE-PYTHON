# CHIA DƯ CHO 42


# đếm các phần tử khác nhau khi chia dư cho 42
if __name__ == '__main__':
    # khởi tạo 1 list rỗng
    a = []

    # Điều kiện nhập
    while len(a) < 10:
        a += list(map(int, input().split()))


    for i in range(len(a)):
        a[i] = a[i] % 42
    cnt = set(a)
    print(len(cnt))
