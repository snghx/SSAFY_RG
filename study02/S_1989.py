# 초심자의 회문 검사

T = int(input())

for tc in range(1, T+1):
    S = str(input())

    if S[:] == S[::-1]:   # 문자열 뒤로 읽기 [::-1]
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')


# 만약 level[::-2]라면 lvl