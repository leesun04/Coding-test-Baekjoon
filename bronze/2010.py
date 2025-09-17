def main():
    N = int(input())
    nums = []
    answer = 0
    for i in range(N):
        nums.append(int(input()))
        if i == N-1:
            break
        else:
            answer += (nums[i]-1)
    answer+=nums[N-1]
    print(answer)
main()