def main():
    answer = list(map(int, input().split()))
    answer.sort()
    print(' '.join(map(str, answer)))
main()