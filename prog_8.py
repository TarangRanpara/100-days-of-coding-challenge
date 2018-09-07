def get_area(n):
    area = None

    if n<=3:
        #no rectangle can be formed
        area = None
        
    elif (n % 4 == 0) or (n % 4 == 1):
        '''
        area = l * b
        if one stick remains unused, we can't do anything about it.
        '''
        area = int(n / 4) * int(n / 4)

    elif n % 4 > 1:
        '''
        remainder will never be greater than 3. 
        so, one-one stick either on l or b can be used and let one get wasted.
        '''
        area  = int(n / 4) * ( int(n / 4) + 1)

    return area

def main():
    l = []
    n = int(input('enter number of inputs:'))
    
    #for proper formatted answer
    for i in range(n):
        l.append(get_area(int(input('enter number of straws:'))))

    print(l)

if __name__ == '__main__':
    main()
