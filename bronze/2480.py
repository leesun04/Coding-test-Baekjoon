def main():
    nums = list(map(int, input().split()))
    answer = 0
    for i in nums:
        if nums.count(i) == 3:
             print(10000+nums[0] * 1000)
             answer+=1
             break
        elif nums.count(i) ==2:
            print(1000+i*100)
            answer+=1
            break
    if answer ==0:
        print(100*max(nums))
main()