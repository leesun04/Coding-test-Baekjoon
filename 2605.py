def main():
    N = int(input())
    students = list(map(int, input().split()))
    answer = []
    for i in range(N):
        if i==0:
            answer.insert(students[i], i+1)
            continue

        answer.insert(students[i], i+1)
    answer.reverse()
    print(' '.join(map(str, answer)))
main()
# def main():
#     N = int(input())
#     students = list(map(int, input().split()))
#     answer = []
#     for i in range(N):
#         if i==0:
#             answer.insert(students[i], i+1)
#             continue

#         answer.insert(i - students[i], i+1)
#     print(' '.join(map(str, answer)))
# main()