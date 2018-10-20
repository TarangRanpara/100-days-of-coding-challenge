def print_n(i,n):
    if i == n:
        print(i,end='\t')
    else:
        print(i,end='\t')
        i += 1
        print_n(i,n)
    

def main():
    print_n(1,int(input()))

if __name__ == '__main__':
    main()
