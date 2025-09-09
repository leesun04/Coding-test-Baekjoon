def main():
    M = int(input())
    answer = [1,2,3]
    for _ in range(M):
        x, y = map(int, input().split())
        num_x = answer.index(x)
        num_y = answer.index(y)
        answer[num_x], answer[num_y] = answer[num_y], answer[num_x]
    print(answer[0])
main()