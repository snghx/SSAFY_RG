
T = int(input())

# a = []
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     a.append(test_case)
#     result = sum(a)
    
# print(result)


# 더 간단한 버전

sum = 0
for t in range(1, T+1):
    sum += t

print(sum)
