def main():
    N = int(input())
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)
    answer = []
    k = 0
    for i in range(N):
        newScore = scores[i]/scores[0]*100
        answer.append(newScore)
        k +=answer[i]
    print(k/N)
main()