def main():
    
    str = input('enter string:')
    max_char,min_char = str[0],str[0]
    
    for x in str:
        if max_char < x:
            max_char = x
        if min_char > x:
            min_char = x

    print('largest:',max_char,'\nsmallest:',min_char)

if __name__ == '__main__':
    main()
