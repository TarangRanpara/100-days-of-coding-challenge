def isPalindrome(abc):
    #Checking if palindrome or not.
    r = ''.join(reversed(abc))
    if r == abc:
        return True
    else:
        return False

def main():
    x = input("enter num:")

    i,diff1 = 1,0
    #going +1 each time until palindrome is found.
    while isPalindrome(str(int(x)+i)) == False:
        diff1 += 1
        i += 1
    
    j,diff2 = 1,0
    #going -1 each time until palindrome is found.
    while isPalindrome(str(int(x)-j)) == False:
        diff2 += 1
        j += 1    

    #showing the result.
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
