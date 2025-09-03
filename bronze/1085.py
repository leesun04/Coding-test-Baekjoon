def main():
    x, y, w, h = map(int, input().split())
    answer = []
    answer.append(abs(0-x))
    answer.append(abs(0-y))
    answer.append(abs(w-x))
    answer.append(abs(h-y))
    print(min(answer))
main()
