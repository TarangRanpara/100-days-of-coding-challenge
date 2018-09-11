def main():
    result = []
    t = int(input('enter t:'))
    
    for i in range(t):
        
        #taking inputs
        n,k = input('enter n & k:').split(' ')
        
        #array of elements
        a = []
        print('enter array:')
        for i in range(int(n)):
            a.append(int(input()))

        #result
        if min(a) < int(k):
            result.append(int(k) - min(a))
        else:
            result.append(0)

    print(result)
    
if __name__ == '__main__':
    main()
