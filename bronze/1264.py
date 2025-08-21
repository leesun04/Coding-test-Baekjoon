def main():
    nums = ["a", "e", "i", "o", "u"]
    while(True):
        answer = 0
        quizs = input().lower()
        quizs_list = list(quizs)
        for i in range(len(quizs_list)):
            if quizs_list[i] in nums:
                answer+=1         
        if quizs == "#":
            break
        print(answer)
main()