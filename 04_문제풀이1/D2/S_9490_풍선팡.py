import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [0, 1, 0, -1] # 우 / 하 / 좌 / 상 방향으로 이동할 경우 바뀔때 활용할 r값
    dc = [1, 0, -1, 0] # 우 / 하 / 좌 / 상 방향으로 이동할 경우 바뀔때 활용할 c값

    result = 0
    for r in range(N):
        for c in range(M):
            pang = tmp = arr[r][c]         # 현재 내 위치에 들어있는 꽃가루 수만큼 터질 수 있다
                                           # pang : 터질 수 있는 꽃가루
                                           # tmp : 터진 꽃가루 합계를 임시로 저장(현재 위치 꽃가루를 저장하고 시작)
            for i in range(4):             # 우/하/좌/상 으로 이동
                for p in range(1, pang+1): # pang만큼 터질 수 있기에 pang을 활용해 이동 거리를 결정
                    nr = r+(dr[i] * p)     # dr / dc에 이를 활용하여 풍선 팡하기
                    nc = c+(dc[i] * p)
                    if (0 <= nr < N) and (0 <= nc < M) : # 범위 안에 있는 경우에만 터진 꽃가루 합계에 해당 값 더하기
                        tmp += arr[nr][nc]
                if result < tmp :          # 전체 결과와 비교하여 더 클 경우에만 갱신하는 방식으로 최대 찾기
                    result = tmp
        
    print(f'#{tc} {result}')               # 출력

