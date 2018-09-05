def find_repeat(string):
    char = None

    for i in range(len(string)):

        #checking for each char's count
        if string.count(string[i]) == 1:
            char = string[i]
            break

    return char


def main():
    print(find_repeat(input('enter string:')))

if __name__ == '__main__':
    main()
