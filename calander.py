c=True
monthcode=[1,4,4,0,2,5,0,3,6,1,4,6]
centuryremcode={100:4,200:2,300:0,0:6}
daylist=['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
loop=True
while loop:
    try:
        date=int(input('Enter Date:'))
        month=int(input('Enter month:'))
        year=int(input('Enter year:'))
    except ValueError:
        print('\nInvalid Input!\nEnter Again\n')
        continue
    if (0<month<13 and 0<date<33):
        c=True
        if month==2:
            if 0<date<29 or 0<date<30:
                c=True
            else:
                print('ENTER CORRECT VALUE!')
                c=False
    else:
        c=False
        print('\nENTER CORRECT VALUE!\n')
    if c:
        for x in range(12):
            if x+1==month:
                monthc=monthcode[x]
        if year%4==0:
            if month==1:
                monthc=0
            elif month==2:
                monthc=3
        century=(year//100)*100
        centuryrem=century%4
        centuryremc=0
        for x in centuryremcode:
            if x==centuryrem:
                centuryremc=centuryremcode[x]
        year1=year%100
        lyear=year1//4
        sum=date+monthc+centuryremc+year1+lyear
        day=sum%7
        for x in range(7):
            if day==x:
                fulldate=str(date)+'/'+str(month)+'/'+str(year)
                print('the day on',fulldate,'is',daylist[x])
        print()
        ans=input('Press [Enter] to Continue')
        print()