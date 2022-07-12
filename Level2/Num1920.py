# 두개의 숫자 리스트를 받아냄
# 두번째 받은리스트원소들이 첫번째 리스트안에 있는지 확인해서 출력

# 이진탐색
def binary_search(ary, key, low, high) :
        if (low <= high) :
            middle = (low + high) // 2
            if key == ary[middle] :
                return 1
            elif (key<ary[middle]) :
                return binary_search(ary, key, low, middle - 1)
            else :
                return binary_search(ary, key, middle + 1, high)
        return None #탐색실패

trial = int(input())
data = list(map(int, input().split()))
data.sort()

trial = int(input())
compare = list(map(int, input().split()))

for i in compare:
    if binary_search(data, i, 0, len(data)-1): print(1)
    else: print(0)
