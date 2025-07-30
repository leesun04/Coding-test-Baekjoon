import sys

def main():
    N = int(sys.stdin.readline()) #입력 변수
    a = 0 #이전 정보를 저장하기 위한 변수
    anwer = 0 #정답 출력 변수
    h = []
    for _ in range(N):
        a = int(sys.stdin.readline())
        h.append(a)
    a = 0
    for _ in range(N):
        k = h.pop()
        if a < k:
            anwer = anwer+1
            a = k
    print(anwer)
main()