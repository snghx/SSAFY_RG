n = int(input())
k = 4*n -3

arr = [[0]*(k) for _ in range(k)]

# 별찍기를 위한 함수 만들기
def my_star(arr,k):
    for r in range(k):
        for c in range(k):
            if r == 0 or r == k:
                arr[r][c] = '*'
    return arr

print(my_star(arr, 2))
            

