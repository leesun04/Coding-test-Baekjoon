def main():
    N = int(input())
    nums = input()
    k = []
    k = "".join(map(str, nums))
    answer =0
    for i in k:
        answer = answer + int(i)
    print(answer)
main()