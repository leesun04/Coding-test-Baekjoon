def main():
    N = int(input())
    passwords = []
    for _ in range(N):
        passwords.append(str(input()))
    reversed_s = [word[::-1] for word in passwords]
    for i in range(len(passwords)):
        if passwords[i] in reversed_s:
            a = passwords[i][len(passwords[i])//2]
            print(f"{len(passwords[i])} {a}")
            break
main()