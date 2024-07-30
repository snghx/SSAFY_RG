# 1948. 날짜계산기 (70m)

T = int(input())

for test_case in range(1, T+1) :
    # 월별 날짜수가 담긴 리스트 생성
    date_list = [31, 28, 31, 30, 31, 30, 31, 31, 31,30,  30, 31]

    a, b, c, d = map(int, input().split())

    if a == c : # 같은 달 사이에서 계산할 경우
        result = d - b +1

    else :
        result = date_list[a-1] -b +1 # 첫 달 중 범위에 속하는 날짜
        for i in range(a, c-1) :      # 첫 달 다음부터 마지막 달 전까지 날짜
            result += date_list[i]
        result += d                   # 마지막달 날짜

    print(f'#{test_case} {result}')

