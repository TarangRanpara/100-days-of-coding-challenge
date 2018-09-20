def get_value(l):
    
    #logic to convert binary into decimal, although it can be done with built-in function too.
    length,sum = len(l),0
    max_power = length - 1
    
    for i in range(length):
        sum += l[i] * (2**(max_power))
        max_power -= 1

    return sum


def main():
    n = int(input('enter n:'))
    #enter 0's & 1's
    l = [int(input()) for i in range(n)]

    pos = -1
    for i in range(len(l)):
        if l[i] == 0:
            l[i] = 1
            pos = i
            break

    if pos!=-1:
        print(get_value(l),pos)
    else:
        print('no modifications needed')
        

if __name__ == '__main__':
    main()
