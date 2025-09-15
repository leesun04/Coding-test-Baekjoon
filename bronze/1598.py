def main():
    # n, m = map(int, input().split())
    # nums = []
    # test = []
    # answer = []
    # answer_m = []
    # for i in range(m+n):
    #     if len(test) == 4:
    #         nums.append(test)
    #         if n in test:
    #             answer.append(test.index(n))
    #             answer.append(nums.index(test))
    #             print(test.index(n))
    #             print(i)
    #             print(nums.index(test))
    #         elif m in test:
    #             answer
    #             answer_m.append(test.index(m))
    #             answer_m.append(nums.index(test))
    #         test = []
    #     test.append(i+1)
    # print(abs(answer[0]-answer_m[0])+ abs(answer[1]-answer_m[1]))
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    print(abs(a // 4 - b // 4) + abs(a % 4 - b % 4))
main()