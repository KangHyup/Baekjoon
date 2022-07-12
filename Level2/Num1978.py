# 소수의 개수를 출력하기

trial = int(input())
data = list(map(int, input().split()))

result = 0

def check_prime(num):
    global result

    if i == 1: return False
    elif i == 2: result +=1

    if i%2 == 0: return False
    else:
        for k in range(i-1, 2, -1):
            if i%k == 0: return False
    return True

for i in data:
    if check_prime(i): result +=1

print(result)
