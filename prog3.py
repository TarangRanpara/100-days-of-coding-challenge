def identify(num):
    sign = {'-':'Negative','0':'Positive','1':'Positive','2':'Positive','3':'Positive','4':'Positive','5':'Positive','6':'Positive','7':'Positive','8':'Positive','9':'Positive'}
    return sign[num[0]]+' Number'

def main():
    print(identify(input("enter num:")))

if __name__ == '__main__':
    main()