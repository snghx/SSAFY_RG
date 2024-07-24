'''1989. 초심자의 회문 검사'''
T = int(input())

for tc in range(1, T+1):
    my_str = input()
    
    # 원래 문자열과 거꾸로 된 문자열을 비교
    if my_str == my_str[::-1]:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))