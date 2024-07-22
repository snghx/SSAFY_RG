# 새로운 불면증 치료법

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    k = 1                     # 처음부터 1번은 세니까, 초기값 1
    s = set()                    # 0~9까지 담을 set 만들기

    while len(s) < 10 :       # len(set) == 10이 되면, 멈추기 
        cnt = k*N             # cnt = 입력 값 * 배수(k)
        for i in str(cnt):    # cnt 문자열로 변환
            s.add(i)          # set자료형에 cnt의 각 자리수 값 추가
        k += 1                # 배수(k)값 +1 증가

    print(f'#{tc} {cnt}')