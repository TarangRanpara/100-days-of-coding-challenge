from itertools import combinations
'''Given five positive integers, find the minimum and maximum values that can be 
   calculated by summing exactly four of the five integers. Then print the respective 
   minimum and maximum values as a single line of two space-separated long integers.
'''
def get_max_min(arr):
    #the noob way - Tjr

    #listing out the possibilities    
    possibility = combinations(arr,4)
    
    l = []
    for i in possibility:
        #appending the sum
        l.append(sum(i))
    
    #returning the max & min of sum
    return max(l),min(l)

def get_max_min_legendary(arr):
    #legendary way - Devansh
    return sum(arr)-min(arr),sum(arr)-max(arr)

def main():
    arr = []
    for i in range(0,5):
        arr.append(int(input('enter no:')))

    max,min = get_max_min(arr)
    print(max,min)

    max,min = get_max_min_legendary(arr)
    print(max,min)

if __name__ == '__main__':
    main()
