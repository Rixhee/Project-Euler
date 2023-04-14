def euler(low, high):

    '''
    low = lower limit
    high = higher limit
    '''
    for num in range(low, high):
        count = 0
        for i in range(1, 21):
            if num % i == 0:
                count += 1
        if count == 20:
            print(num)

if __name__ == "__main__":
    euler(2, 240000000)
    # print(count)
    # final_value = 0
    # for i in count:
    #     if count.count(i) == 10:
    #         final_value = i
    # print(i)
                

        
        
             

