# # 두개의 숫자열
# 17분 시작
# 3개값과 비교하여 결과값을 구하는 함수 만들기
def calculate(mi, ma, ci_ma):  # ci_mx : mx의 변경되는 시작 값
    ans = 0
    for i in range(len(mi)):
        ans = mi[i] + ma[ci_ma+i]

    return ans



T = int(input())

for tc in range(1, T+1):
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))

    if len(list_a) > len(list_b) : mi, ma = list_b, list_a
    if len(list_b) > len(list_a) : mi, ma = list_a, list_b

    ans_max = 0     # 최댓값 초기 설정 : 0

    # 짧은 것 mi , 긴 것 ma
    for i in range(i, len(ma)- len(mi)):
        temp_max = calculate(mi, ma, i)

        if temp_max > ans_max : ans_max = temp_max

    print('#{tc} {ans_max}')

        
    
