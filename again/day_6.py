def main():
    days,years,weeks  = int(input('enter days:')),0,0

    if days > 365:
        years = int(days/365)
    
    if years != 0:
        weeks = 52 * years
    else:
        i=0
        while days > 7:
            days -= 7
            weeks += 1

    print('years:',years,'\nWeeks',weeks,'\nremaining days:',days%365)

    

if __name__ == '__main__':
    main()