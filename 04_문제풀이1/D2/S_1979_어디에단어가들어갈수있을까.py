import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N,K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0 # 단어가 들어갈 수 있는 자리 수 합 기록 
              # 정확하게 흰색 부분이 단어의 길이와 같아야만 단어 입력 가능

    # 행탐색 
    for r in range(N):
        tmp = 0                    # 지금까지 1이 나온 횟수를 임시로 기록
        for c in range(N):
            if arr[r][c] == 1:     # 행을 순회하며 1인 곳 찾기
                tmp += 1           # 지금까지 1이 나온 횟수에 +=1
            else:                  # 0을 만나면
                if tmp == K:       # 지금까지 나온 1의 횟수를 확인. 단어의 길이와 같을 때만 
                    total +=1      # total에 기록
                tmp = 0            # tmp 초기화
        if tmp == K:               # 행의 마지막까지 돌았을 때 확인
            total +=1              # 단어의 길이와 같을 경우 total에 기록
    
    # 열탐색
    for c in range(N):
        tmp = 0
        for r in range(N):
            if arr[r][c] == 1:
                tmp += 1
            else :
                if tmp == K:
                    total += 1
                tmp = 0
        if tmp == K:
            total += 1

    print(f'#{tc} {total}')