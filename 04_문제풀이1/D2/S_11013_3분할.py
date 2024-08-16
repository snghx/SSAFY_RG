import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    result = 10000   # 최종 결과 (임시로 큰 수를 지정)

    for i in range(1, N-1):
        for j in range(i+1,N):
            sum1 = sum(lst[:i])             # 각 구간에 속한 값들의 합계 계산
            sum2 = sum(lst[i:j])
            sum3 = sum(lst[j:])

            max_sum = max(sum1, sum2, sum3) # 구간의 합 중 최대 구하기
            min_sum = min(sum1, sum2, sum3) # 구간의 합 중 최소 구하기

            tmp = max_sum - min_sum         # 최대 / 최소 차이 구하기

            if result > tmp:                # 최대 / 최소 차이가 최소가 되는 경우를 찾는 것이기 때문에
                result = tmp                # 더 작은 경우를 찾을 경우 갱신

    print(f'#{tc} {result}')