def main():
    s = input('enter string')

    #finding distincts
    l = [s[0]]
    for i in range(1,len(s)):
        chr = s[i]
        if chr not in l:
            l.append(chr)

    #finding max occuring char & its count
    max,max_chr = 1,None
    for i in l:
        counts = s.count(i)
        if counts > max:
            max,max_chr = counts,i

    print(max_chr,max)

if __name__ == '__main__':
    main()
