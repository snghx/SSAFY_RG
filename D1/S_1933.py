# 1933번 간단한 N의 약수


T = int(input())
div = []
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    if T % test_case == 0:
        div.append(test_case)
    div.sort()

for i in div:
    print(i, end =" ")
# print(div)