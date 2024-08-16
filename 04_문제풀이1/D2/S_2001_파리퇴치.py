import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())                # N: 배열의 크기 / M: 파리채의 크기 

    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0   # 최종 결과
    for r in range(N):
        for c in range(N):
            tmp = 0                                 # 전체 arr을 순회하며 죽은 파리 수를 구하기 
            for i in range(r,r+M):                  # 파리채의 row 범위 (시작위치 ~ 파리채 크기만큼)
                for j in range(c,c+M):              # 파리채의 col 범위 (시작위치 ~ 파리채 크기만큼)
                    if (0<= i < N) and (0<= j < N): # 파리채가 배열 안에 있을 경우에만 
                        tmp += arr[i][j]            # tmp에 파리채로 잡은 파리 수를 더하기
            if result < tmp:                        # 한 번 파리채로 잡은 파리 수 합계를 활용해 더 많이 잡았을 경우 갱신
                result = tmp

    print(f'#{tc} {result}')
            