def main():
    a = input('enter string:')

    for i in range(0,len(a)):
        #checking if it is lower case
        if a[i].islower():
            #converting
            a = a.replace(a[i], a[i].upper())
        
        #checking if it is upper case
        elif a[i].isupper():
            #converting
            a = a.replace(a[i],a[i].lower())

    print(a)

if __name__ == '__main__':
    main()