def main():
    L, P = map(int, input().split())
    paper = list(map(int, input().split()))
    answer = L*P
    paper_answer =[]
    for i in range(len(paper)):
        paper_answer.append(paper[i]-answer)
    print(' '.join(map(str, paper_answer)))
main()