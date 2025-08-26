def main():
    N = int(input())
    stars = "*"
    for i in range(N, 0, -1):
        print(i)
        print(stars*i)
main()