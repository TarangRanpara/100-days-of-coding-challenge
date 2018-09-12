def is_anagram(str1,str2):
    op = False

    #checking for length
    if len(str1) == len(str2):

        #Setting counter
        ctr=0
        for i in range(len(str1)):
            if str1[i] in str2:
                #checking for each char
                ctr += 1
        
        if len(str1)==ctr:
            op = True

    return op

def main():

    for i in range(int(input('enter number of strings:'))):
        #iterating n times
        print(is_anagram(input('enter string-1:').lower(),input('enter string-2:').lower()))

if __name__ == '__main__':
    main()
