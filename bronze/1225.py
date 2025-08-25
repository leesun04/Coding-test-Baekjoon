import sys
def main():
    A, B = map(str, sys.stdin.readline().split())
    answer = 0
    for a in A:
        for b in B:
            answer += int(a) * int(b)
    print(answer)
main()