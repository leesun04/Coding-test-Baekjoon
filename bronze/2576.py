def main():
    N = []
    nums = []
    for i in range(7):
        N.append(int(input()))
        if N[i] % 2 != 0:
            nums.append(N[i])
    if len(nums) == 0:
        print(-1)
    else:
        nums.sort()
        print(sum(nums))
        print(nums[0])
main()