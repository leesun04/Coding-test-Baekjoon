def main():
    N = int(input())
    F = int(input())
    pre_num = N // 100
    end_num = N % 100

    for i in range(100):
        pre_answer = ""
        if i < 10:
            pre_answer = str(pre_num)+"0"+str(i)
        else:
            pre_answer = str(pre_num)+str(i)
        if int(pre_answer) % F ==0:
            if i < 10:
                print(f"0{i}")
            else:
                print(i)
            break

main()