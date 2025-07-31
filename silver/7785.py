def main():
    n = int(input())
    names = {}
    for _ in range(n):
        key, value = input().split()
        if value == "leave":
            del names[key]
        else:
            names[key] = value
    
    for i in sorted(names, reverse=True):
        print(i)
        
main()