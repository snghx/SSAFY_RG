'''2025. N줄덧셈'''
T = int(input())

for test_case in range(1, T):
    T += test_case  # T에게 test_case(1 ~ T-1까지)를 더함
print(T)