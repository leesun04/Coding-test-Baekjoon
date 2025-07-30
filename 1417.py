def main():
    N =int(input())
    numbers = []
    for i in range(N):
        numbers[i] = int(input())
    print(' '.join(map(int, numbers)))
main()