# 2070. 큰 놈, 작은 놈, 같은 놈 (15m)

T = int(input())

def my_compare(a, b) : # 값을 비교하는 함수 작성
    if a > b :
        return '>'
    if a == b :
        return '='
    if a < b :
        return '<'

for test_case in range(1, T+1):
    a, b = map(int, input().split())
    print(f'#{test_case} {my_compare(a, b)}')