def main():
    N = int(input())
    nums = list(map(int, input().split()))
    y_nums = []
    m_nums = []
    for i in range(N):
        y_nums.append((nums[i]//30+1)*10)
        m_nums.append((nums[i]//60+1)*15)

    if sum(y_nums) < sum(m_nums):
        print(f"Y {sum(y_nums)}")
    elif sum(y_nums) > sum(m_nums):
        print(f"M {sum(m_nums)}")
    else:
        print(f"Y M {sum(y_nums)}")
main()