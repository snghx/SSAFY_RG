# 1948. 날짜 계산기
# 3:44시작 3:50종료

T = int(input())

m_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9: 30, 10:31, 11:30, 12:31}

for t in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())

    ans = 0

    if m1 == m2:
        ans = d2 - d1 + 1
    else:
        ans = (m_dict[m1] - d1 +1 ) + d2
        for i in range(m1+1, m2):
            ans += m_dict[i]
    
    print(f'#{t} {ans}')