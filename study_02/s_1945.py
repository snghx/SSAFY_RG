T = int(input())

for tc in range(1, T+1):
    NUM = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    while NUM != 1:
        if NUM % 2 == 0:
            a += 1
            NUM = NUM / 2
        elif NUM % 3 == 0:
            b += 1
            NUM = NUM / 3
        elif NUM % 5 == 0:
            c += 1
            NUM = NUM / 5
        elif NUM % 7 == 0:
            d += 1
            NUM = NUM / 7
        elif NUM % 11 == 0:
            e += 1
            NUM = NUM / 11
    print(f'#{tc}', a, b, c, d, e)