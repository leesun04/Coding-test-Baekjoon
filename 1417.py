def main():
    N =int(input())
    dasom = int(input())
    numbers = []
    answer = 0
    if(N ==1):
        print(answer)
    else:
        for _ in range(N-1):
            numbers.append(int(input()))
        while(True):
            numbers.sort(reverse=True)
            if numbers[0] < dasom:
                break
            numbers[0]-=1
            dasom+=1
            answer+=1
        print(answer)

main()