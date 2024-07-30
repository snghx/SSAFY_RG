'''1966. 숫자를 정렬하자 / 20분'''
T = int(input())

num_list = []

for tc in range(1, T+1):
    N = int(input())
    nums = sorted(list(map(int, input().split()))) # 받은 수들을 정렬

    print('#{}'.format(tc), end=' ')    # 아래 nums의 첫자리만 나와 따로 출력 후, end=' '로 한 줄 출력
    print(*nums)                        # list를 언패킹