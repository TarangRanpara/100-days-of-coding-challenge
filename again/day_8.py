def main():
    l = [int(input()) for i in range(int(input('enter array length:')))]
    
    for i in range(min(l),max(l)):
        if i not in l:
            print(i,end='\t')

if __name__ == '__main__':
    main()ss
