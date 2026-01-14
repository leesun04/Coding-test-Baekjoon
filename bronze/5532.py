def main():
    L = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    math = A // C
    korea = B // D
    if A % C !=0:
        math +=1
    if B % D !=0:
        korea+=1
    if L - math < L - korea:
        print(L-math)
    elif L - math < L - korea:
        print(L-korea)
    else:
        print(L-korea)
main()