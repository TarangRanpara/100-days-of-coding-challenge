def main():
    #entering list
    l = input('enter list:').split()

    #containers
    pos,neg,result = [],[],[]
    for i in l:
        if int(i) > 0:
            pos.append(i)
        else:
            neg.append(i)

    #arranging
    posi,posn = 0,0
    for i in range(len(l)):
        if i%2 != 0:
            result.append(pos[posi])
            posi += 1
        else:
            result.append(neg[posn])
            posn += 1

    print(result)




if __name__ == '__main__':
    main()
