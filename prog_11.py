def main():
    s = input('enter string:')
    result = ''

    for char in s:
        if (char not in result):
            result += char 

    print(result)

if __name__ == '__main__':
    main()
