# 대각선 출력하기


for p in range(5):
    line = ['+']*5
    # p는'#'으로 바꿀 포인트 지점
    line[p] = '#'
    print(*line, sep ='')



''' 2중 for문으로 풀기
for i in range(1,6):
    for j in range(1,6):
        if j == i : 
            print('#', end='')
        else: print('+', end='')
        j += 1
    print()

'''