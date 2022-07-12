# 단어정렬하기
# 1. 단어가 짧은순으로 정렬 2. 길이가 같을시 사전순으로

class Node:
    def __init__(self, word):
        self.word = word
        self.length = len(word)

def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low].length < pivot.length or (arr[low].length == pivot.length and arr[low].word < pivot.word):
                low += 1
            while arr[high].length > pivot.length or (arr[high].length == pivot.length and arr[high].word > pivot.word):
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)

trial = int(input())
data = []
for _ in range(trial):
    data.append(Node(input().strip()))

quick_sort(data)
for i in data:
    print(i.word)

