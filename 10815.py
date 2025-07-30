import sys

def main():
    N = int(sys.stdin.readline())
    cards = list(map(int, input().split()))
    M = int(sys.stdin.readline())
    nums = list(map(int, input().split()))

    cards.sort()
    answer = []
    for i in range(M):
        answer.append(binary_search(cards, nums[i]))
    print(' '.join(map(str, answer)))

def binary_search(arr, target): #이진탐색
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0  

main() 