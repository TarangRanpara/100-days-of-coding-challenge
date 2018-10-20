def main():
    
    for test in range(int(input('enter number of test cases:'))):
        
        l = [int(input()) for j in range(int(input('enter number of elements:')))]
        
        #if all elements are equal
        if not l[1:] == l[:-1]:
            n,ctr = len(l),0
            
            for i in range(n):
                ctr = 0
                
                for j in range(n):
                    if l[i] >= l[j]:
                        ctr += 1

                if ctr-1 == n-2:
                    print(l[i])
                    break
        
        else:
            print(l[0])

if __name__ == '__main__':
    main()
