# 2007. 패턴 마디의 길이
# 도움을 준 정다인씨 very thx

T = int(input())

for t in range(1, T+1):
    txt = input()

    for i in range(len(txt)):
        if txt[:i] == txt[i:(2*i)] and len(txt[:i]) != 0:
            print(len(txt[:i]))
            break