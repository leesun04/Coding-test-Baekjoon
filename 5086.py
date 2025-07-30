def main():
    while True:
        N, X = map(int, input().split())
        
        if X == 0 and N ==0:
            break
        elif X % N == 0:
            print("factor")
        elif N % X == 0:
            print("multiple")
        else:
            print("neither")
main()