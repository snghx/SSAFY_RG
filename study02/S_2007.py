# 2007 패턴 마다의 길이

T = int(input())

for tc in range(1, T+1):
    string = str(input())

    for i in range(1,11):
        if string[:i] == string[i:2*i]:
            print(f'#{tc} {i}')
            break