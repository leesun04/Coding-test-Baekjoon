def str_list(names):
    if names == "black":
        s =0
        k = 1
    elif names == "brown":
        s = 1
        k = 10
    elif names == "red":
        s = 2
        k = 100
    elif names == "orange":
        s = 3
        k = 1000
    elif names == "yellow":
        s = 4
        k = 10000
    elif names == "green":
        s = 5
        k = 100000
    elif names == "blue":
        s = 6
        k = 1000000
    elif names == "violet":
        s = 7
        k = 10000000
    elif names == "grey":
        s = 8
        k = 100000000
    elif names == "white":
        s = 9
        k = 1000000000
    return s, k

def main():
    n = input()
    n1, n2 = str_list(n)    
    m = input()
    m1, m2 = str_list(m)
    c = input()
    c1,c2 = str_list(c)
    answer_pre = str(n1)+str(m1)
    answer = int(answer_pre) * c2
    print(answer)
main()
