import sys
def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        answer = 1
        a, b = map(int, sys.stdin.readline().split())
        answer = pow(a, b, 10) #거듭제곱 구하는 함수
        if answer == 0:
            print(10)
        else:
            print(answer) 
main()