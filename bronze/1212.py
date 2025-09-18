import sys

def main():
    N = sys.stdin.readline().strip()
    nums = list(map(int, N))
    answer = []
    for i in range(len(nums)):
        answer.append(logic(nums[i]))
    result = ''.join(answer)
    print(int(result))

def logic(a):
    if a==0:
        return "000"
    elif a == 1:
        return "001"
    elif a == 2:
        return "010"
    elif a==3:
        return "011"
    elif a==4:
        return "100"
    elif a==5:
        return "101"
    elif a==6:
        return "110"
    elif a==7:
        return "111"
main()