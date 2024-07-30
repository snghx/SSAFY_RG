# 1989. 초심자의 회문 검사 (3m)

T = int(input())

for test_case in range(1, T+1) :
    text = list(input())

    if text[::-1] == text :
        result = 1
    else :
        result = 0
    
    print(f'#{test_case} {result}')