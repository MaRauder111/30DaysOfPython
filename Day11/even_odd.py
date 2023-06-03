def evens_and_odds(num):
    count_even = 0
    count_odd = 0
    for i in range(num+1):
        if i%2 == 0:
            count_even += i
        else:
            count_odd += i
    print(count_even,count_odd)

evens_and_odds(100)