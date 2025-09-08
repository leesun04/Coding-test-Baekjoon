def main():
    while True:
        N = input()
        if N == "0":
            break
        answer = []
        for i in N:
            if i == "1":
                answer.append(2)
            elif i == "0":
                answer.append(4)
            else:
                answer.append(3)
        
        answer.append((len(N)-1)+2)
        print(sum(answer))
main()