from collections import deque
q = deque([])
answer = []
nums = []
def main():
    N = int(input())
    k=0
    for i in range(N):
        q.append(i+1)

    while(True):
        if len(q) ==1:
            answer.append(q.popleft())
            break
        if (k+1) % 2 !=0: 
            answer.append(q.popleft())
        elif (k+1) % 2 ==0:
            q.append(q.popleft())
        k+=1

    print(' '.join(map(str, answer)))
    k+=1
main()