def isPalindrome(abc):
    r = ''.join(reversed(abc))
    if r == abc:
        return True
    else:
        return False

def main():
    x = input()

    i=1
    diff1 = 0
    while isPalindrome(str(int(x)+i)) == False:
        diff1 += 1
        i += 1
    
    j=1
    diff2 = 0
    while isPalindrome(str(int(x)-j)) == False:
        diff2 += 1
        j += 1    

    if isPalindrome(x):
        print(x,' is a Palindrome number')
    else:
        print(x,' is not a Palindrome number')
        
    if min([diff1,diff2]) == diff1:
        print(int(x) + i,' is a nearest palindrome number.')
    else:
        print(int(x) - j,' is a nearest palindrome number.')

if __name__ == '__main__':
    main()
