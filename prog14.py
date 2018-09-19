def cube(n,power):

    #terminating condition
    if power==1:
        return n
    
    #recursive condition
    else:
        return n*cube(n,power-1)

def main():
    print(cube(int(input('enter no:')),3))

if __name__ == '__main__':
    main()