def main():
    N = int(input())
    nums = []
    for i in range(N):
        nums.append(input())
    for i in range(N):
        print(f"{i+1}. {nums[i]}")
main()