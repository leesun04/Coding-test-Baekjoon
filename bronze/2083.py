def main():
    while(True):
        n, m, k = map(str, input().split())
        if int(m) > 17 or int(k) >=80:
            answer = "Senior"
        else:
            answer = "Junior"
            
        if n == "#" and int(m) == 0 and int(k) == 0:
            break
        print(f"{n} {answer}")
main()