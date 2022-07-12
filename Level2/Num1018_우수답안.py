#체스판
import sys
read = sys.stdin.readline

n,m = map(int, read().split())

box = [[0 for _ in range(m+1)] for _ in range(n+1)] #리스트초기화: mxn크기의 원소가 싹다 0인 리스트를 만듦

for i in range(n):
    s = read().strip()
    for j in range(m):
        tmp = (i+j)%2
        if s[j] == 'B':
            tmp = 1-tmp
        box[i+1][j+1] = box[i][j+1] + box[i+1][j] - box[i][j] + tmp

max_v = 32
for i in range(8, n+1):
    for j in range(8, m+1):
        x = box[i][j] + box[i-8][j-8] - box[i][j-8] - box[i-8][j]
        if x > 32:
            x = 64 - x
        if x < max_v:
            max_v = x
print(max_v)