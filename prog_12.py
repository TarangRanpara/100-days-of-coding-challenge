def main():
    result = []
    for i in range(int(input('enter no of test case:'))):
        l = []
        for j in range(int(input('enter list size:'))):
            l.append(int(input('element:')))
        
        for j in l:
            if l.count(j) == 1:
                result.append(j)
                break
    
    print(result)

if __name__ == '__main__':
    main()
