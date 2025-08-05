import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    n_nums = list(map(int, sys.stdin.readline().split()))
    sum_nums = [0] * (N+1)

    for i in range(1,N+1):
        sum_nums[i] = sum_nums[i-1]+n_nums[i-1]

    for _ in range(M):
        i, j = map(int, sys.stdin.readline().split())
        answer = sum_nums[j] - sum_nums[i-1]
        print(answer)
main()