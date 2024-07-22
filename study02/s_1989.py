# 1989. 초심자의 회문 검사
# 9:14 시작 9:16 종료

T = int(input())

for t in range(1, T+1):
    txt = input().strip() #양쪽 공백 제거
    
    if txt == txt[::-1]: #입력받은 문자열이 역순으로 출력한 문자열과 같다면
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")