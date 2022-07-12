# 1부터 N장의 카드가 있음
# 맨위가1, 맨밑이 n임
# 카드가 한장남을때 까지 맨위의 카드를 버리고, 다음카드를 맨밑에 놓는행위를 반복
# 마지막으로 남는카드?
# 리스트로 del함수쓰면 시간초과나서 deque써야함

from collections import deque

howmany = int(input())
queue = deque()

for i in range(1, howmany+1):
    queue.append(i)

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])

