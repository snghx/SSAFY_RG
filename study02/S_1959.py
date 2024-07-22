# # 두개의 숫자열

# 3개값과 비교하여 결과값을 구하는 함수 만들기
def calculate(mi, ma, ci_ma):  # ci_mx : mx의 변경되는 시작 값
    ans = 0
    for i in range(len(mi)):   
        ans += mi[i]*ma[ci_ma+i]  
    return ans


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))

    # 2개의 리스트 중 짧은 리스트 정하기
    if N > M : mi, ma = list_b, list_a
    else: mi, ma = list_a, list_b

    ans_max = 0                             # 최댓값 초기 설정 : 0

    # 짧은 것 mi , 긴 것 ma
    for i in range(len(ma)- len(mi) + 1):
        temp_max = calculate(mi, ma, i)
        
        ans_max = max(temp_max, ans_max)    # 큰 값 업데이트

    print(f'#{tc} {ans_max}')

        





''' 그냥 풀기
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

	# 누가 더 긴건지
    if N < M:
        s = a_list
        l = b_list
    else:
        s = b_list
        l = a_list
        
    ans_max=0

    for k in range(len(l)-len(s)+1):
        ans_sum = 0
        for i in range(len(s)):
            ans_sum += s[i]*l[i+k]

        ans_max = max(ans_sum, ans_max)

    print(f'#{test_case} {ans_max}')

'''
