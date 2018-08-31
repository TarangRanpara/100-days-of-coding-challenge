from random import randint

'''
You are in charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age.
When she blows out the candles, she’ll only be able to blow out the tallest ones. 
Your task is to find out how many candles she can successfully blow out.
'''

def get_counts(age):
    l = [randint(1,4) for i in range(age)]
    return l.count(max(l))
    
def main():
    print(get_counts(int(input('enter age:'))))

if __name__ == '__main__':
    main()
