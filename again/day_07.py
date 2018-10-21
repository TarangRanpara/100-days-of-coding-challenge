def main():
    s,n= input('enter string:'),int(input('enter n:'))

    if n <= len(s):
        print(s[:n].count('a'))

    else:
        repeat = int(n/len(s))
        print(repeat*(s.count('a')) + s[:(n % len(s))].count('a'))

if __name__ == '__main__':
    main()
