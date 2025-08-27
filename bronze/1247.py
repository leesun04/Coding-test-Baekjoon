def main():
    for _ in range(3):
        N = int(input())
        nums = []
        for _ in range(N):
            a = int(input())
            nums.append(a)
        answer = sum(nums)
        if answer == 0:
            print(0)
        elif answer < 0:
            print("-")
        else:
            print("+")
main()