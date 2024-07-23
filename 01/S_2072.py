# 2072. 홀수만 더하기 (20m)

T = int(input())

for test_case in range(1, T+1) :
    numbers = list(map(int, input().split()))
    odd_list = [] # 홀수만 담을 빈 리스트 생성

    for i in numbers :
        if i % 2 != 0 :
            odd_list.append(i) # 홀수일 경우에만 리스트에 해당 값 넣기
        else :
            pass               # 짝수일 경우 pass

    result = sum(odd_list)     # 홀수만 모은 리스트 값 더하기
    print(f'#{test_case} {result}')