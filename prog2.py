from random import randint

def get_counts(age):
    l = [randint(1,4) for i in range(age)]
    return l.count(max(l))
    
def main():
    print(get_counts(int(input('enter age:'))))

if __name__ == '__main__':
    main()
