# 단어정렬하기
# 1. 단어가 짧은순으로 정렬 2. 길이가 같을시 사전순으로

def sort_word(ary):
    def sort(low, high):
        if high <= low:
            return
    
        mid = partition(low, high)
        sort(low, mid-1)
        sort(mid, high)
    
    def partition(low, high):
        pivot = ary[(low+high) //2]
        while low <= high:
            while len(data[low]) < len(pivot) or (len(data[low]) == len(pivot)and data[low] < pivot) :
                low += 1
            while len(data[high]) > len(pivot) or (len(data[high]) == len(pivot) and data[high] > pivot):
                high -=1
            
            if low <= high:
                data[low], data[high] = data[high], data[low]
                low , high = low+1, high-1
        return low

    return sort(0, len(ary)-1)
        
trial = int(input())
data = []

for i in  range(trial):
    word = input()
    if word not in data:
        data.append(word)

sort_word(data)
for i in data:
    print(i)