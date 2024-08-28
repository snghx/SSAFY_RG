import sys
sys.stdin = open('input.txt')

n = int(input())

alpha_dict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5,
              'F':6, 'G':7, 'H':8, 'I':9, 'J':10,
              'K':11, 'L':12, 'M':13, 'N':14, 'O':15,
              'P':16, 'Q':17, 'R':18, 'S':19, 'T':20,
              'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

# 함수 정의
# 전위 순회
def preorder_traversal(v):
    global result

    if v == 0:
        return ''
    
    idx = v
    result = T[idx]
    result += preorder_traversal(L[idx])
    result += preorder_traversal(R[idx])
    return result

# 중위 순회
def inorder_traversal(v):
    global result

    if v == 0:
        return ''
    
    idx = v
    result = inorder_traversal(L[idx])
    result += T[idx]
    result += inorder_traversal(R[idx])
    return result

# 후위 순회
def postorder_traversal(v):
    global result

    if v == 0:
        return ''
    
    idx = v
    result = postorder_traversal(L[idx])
    result += postorder_traversal(R[idx])
    result += T[idx]
    return result

L = [0]*(n+1)
R = [0]*(n+1)
T = [0]*(n+1) 

for _ in range(n):
    node, l, r = input().split()

    T[alpha_dict[node]] = node

    if l != '.':
        L[alpha_dict[node]] = alpha_dict[l]
    if r != '.':
        R[alpha_dict[node]] = alpha_dict[r]

result = ''

print(preorder_traversal(alpha_dict['A']))
print(inorder_traversal(alpha_dict['A']))
print(postorder_traversal(alpha_dict['A']))
