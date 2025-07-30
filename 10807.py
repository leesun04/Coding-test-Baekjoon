def main():
    cnt = 0
    N = int(input())
    nums = list(map(int, input().split()))
    v = int(input())
    for i in range(len(nums)):
        if v == nums[i]:
            cnt+=1
    print(cnt)
main()
