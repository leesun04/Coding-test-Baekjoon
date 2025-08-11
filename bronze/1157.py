def main():
    N = input().lower()
    world_list = list(set(N))
    answer = []
    
    for i in world_list:
        nums = N.count(i)
        answer.append(nums)
    
    max_count = max(answer)
    
    if answer.count(max_count) >= 2:
        print("?")
    else:
        print(world_list[answer.index(max_count)].upper())
main()