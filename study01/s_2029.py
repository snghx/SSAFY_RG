# 2029. 몫과 나머지 출력하기

T = int(input())

for t in (1, T+1):
    a, b = map(int, input().split()) # 3 16으로 input값이 들어오면 a에는 3, b에는 16을 저장

    print(f"#{t} {a//b} {a%b}")
