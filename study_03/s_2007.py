'''2007. 패턴 마디의 길이 / (20분)'''
T = int(input())

for tc in range(1, T+1):
    my_strs = list(map(str, input()))   # 문자열을 list로 받음

    for s in range(len(my_strs)):
        if my_strs[:s] == my_strs[s:s*2]:       # s 이전까지와 s ~ 2s 이전이 같을 때
            if 1 <= s <= 10:                    # 그 s가 1 ~ 10까지의 범위를 가진다면
                print('#{} {}'.format(tc, s))   # s를 출력하고 break / s가 5 -> 10까지 나올 경우를 제외
                break