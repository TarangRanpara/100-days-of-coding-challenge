def main():
    result = ''
    for i in input('enter string:'):
        if i.isalpha():
            result += i

    print(result)

if __name__ == '__main__':
    main()
