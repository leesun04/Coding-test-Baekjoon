def main():
    N = int(input())
    cnt = 1
    start = 1
    end = 1
    sums = 1
    while(end !=N):
        if N == 1:
            break
        if sums < N:
            end+=1
            sums = sums+end
        elif sums == N:
            cnt+=1
            end+=1
            sums = sums+end
        elif sums > N:
            sums = sums-start
            start+=1
    print(cnt)
main()