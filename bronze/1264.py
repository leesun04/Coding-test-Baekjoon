def main():
    nums = ["a", "e", "i", "o", "u"]
    while(True):
        quizs = input()
        if nums in quizs:
            print(1)
        elif quizs == "#":
            break
main()