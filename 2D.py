import random

def result():
    r=' ==================== \n'
    for a in range(10):
        r+='|'
        for b in range(10):
            r+=l[b][a]+'.'
        r+='|'
        r+='\n'
    r+=' ===================='
    return r

def near():
    f=False
    global xm,xp,ym,yp
    p='you are near!'
    q='you are very close'
    if abs(xm-xp)==1 or abs(ym-yp)==1:
        print(q)
    if abs(xm-xp)==2 or abs(ym-yp)==2:
        print(p)
    if -1<xm+1<10 and -1<ym+1<10:
        if l[ym+1][xm+1]=='y' or l[ym+1][xm-1]=='y':
            print(q)
        elif l[ym-1][xm+1]=='y' or l[ym-1][xm-1]=='y':
            print(q)
    else:
        xm=9
        ym=9
        if l[ym+1][xm+1]=='y' or l[ym+1][xm-1]=='y':
            print(q)
        elif l[ym-1][xm+1]=='y' or l[ym-1][xm-1]=='y':
            print(q)
    if -1<xm-1<10 and -1<ym-1<10:
        if l[ym+1][xm+1]=='y' or l[ym+1][xm-1]=='y':
            print(q)
        elif l[ym-1][xm+1]=='y' or l[ym-1][xm-1]=='y':
            print(q)
    else:
        xm=0
        ym=0
        if l[ym+1][xm+1]=='y' or l[ym+1][xm-1]=='y':
            print(q)
        elif l[ym-1][xm+1]=='y' or l[ym-1][xm-1]=='y':
            print(q)
    if -1<xm+2<10 and -1<ym+2<10:
        if l[ym+2][xm+2]=='y' or l[ym+2][xm-2]=='y':
            print(q)
        elif l[ym-2][xm+2]=='y' or l[ym-2][xm-2]=='y':
            print(q)
    else:
        xm=9
        ym=9
        if l[ym+2][xm+2]=='y' or l[ym+2][xm-2]=='y':
            print(q)
        elif l[ym-2][xm+2]=='y' or l[ym-2][xm-2]=='y':
            print(q)
    if -1<xm-2<10 and -1<ym-2<10:
        if l[ym+2][xm+2]=='y' or l[ym+2][xm-2]=='y':
            print(q)
        elif l[ym-2][xm+2]=='y' or l[ym-2][xm-2]=='y':
            print(q)
    else:
        xm=0
        ym=0
        if l[ym+2][xm+2]=='y' or l[ym+2][xm-2]=='y':
            print(q)
        elif l[ym-2][xm+2]=='y' or l[ym-2][xm-2]=='y':
            print(q)
    if vis%3!=0:
        print('status: Invisible')
        print('It will be visible in (',3-vis%3,') moves')
    else:
        print('status: Visible')
    
def found():
    if abs(xm-xp)==0 and abs(ym-yp)==0:
        print('you found it!')
        print('your score:',score)
        c=0
    else:
        c=1
    return c

loop=True
while loop:
    xp,yp=0,0
    xm=random.randint(1,10)
    ym=random.randint(1,10)
    c=1
    r=''
    l=[]
    vis=0
    score=0
    v=1
    for x in range(10):
        l.append([' ',' ',' ',' ',' ',' ',' ',' ',' ',' '])
        l[0][0]='y'
    while c==1:
        score+=c
        vis+=1
        r=result()
        ans=input(r)
        print()
        ans1=ans.upper()
        if len(ans1)>=2 and ans1.endswith('L'):
            num=int(ans1[0])
            if 10>num>-1:
                l[xp][yp]=' '
                l[xm][ym]=' '
                xp-=num
                if 10>xp>-1:
                    xm=random.choice((xm-1,xm,xm+1))
                    ym=random.choice((ym-1,ym,ym+1))
                    if vis%3==0:
                        l[xm][ym]='x'
                    else:
                        l[xm][ym]=' '
                    l[xp][yp]='y'
                    near()
                    c=found()
                else:
                    xp=0
                    xm=random.choice((xm,xm+1))
                    ym=random.choice((ym,ym+1))
                    if vis%3==0:
                        l[xm][ym]='x'
                    else:
                        l[xm][ym]=' '
                    l[xp][yp]='y'
                    near()
                    c=found()
            else:
                print('Enter correct value!')
                print('Digit from 1 to 9 are valid')
                score-=1
        elif len(ans1)>=2 and ans1.endswith('R'):
            num=int(ans1[0])
            if 10>num>-1:
                l[xp][yp]=' '
                l[xm][ym]=' '
                xp+=num
                if 10>xp>-1:
                    xm=random.choice((xm-1,xm,xm+1))
                    ym=random.choice((ym-1,ym,ym+1))
                    if vis%3==0:
                        l[xm][ym]='x'
                    else:
                        l[xm][ym]=' '
                    l[xp][yp]='y'
                    near()
                    c=found()
                else:
                    xp=9
                    xm=random.choice((xm,xm-1))
                    ym=random.choice((ym,ym-1))
                    if vis%3==0:
                        l[xm][ym]='x'
                    else:
                        l[xm][ym]=' '
                    l[xp][yp]='y'
                    near()
                    c=found()
            else:
                print('Enter correct value!')
                print('Digit from 1 to 9 are valid')
                score-=1
        elif len(ans1)>=2 and ans1.endswith('U'):
            num=int(ans1[0])
            if 10>num>-1:
                l[xp][yp]=' '
                l[xm][ym]=' '
                yp-=num
                if 10>yp>-1:
                    xm=random.choice((xm-1,xm,xm+1))
                    ym=random.choice((ym-1,ym,ym+1))
                    if vis%3==0:
                        l[xm][ym]='x'
                    else:
                        l[xm][ym]=' '
                    l[xp][yp]='y'
                    near()
                    c=found()
                else:
                    yp=0
                    xm=random.choice((xm,xm+1))
                    ym=random.choice((ym,ym+1))
                    if vis%3==0:
                        l[xm][ym]='x'
                    else:
                        l[xm][ym]=' '
                    l[xp][yp]='y'
                    near()
                    c=found()
            else:
                print('Enter correct value!')
                print('Digit from 1 to 9 are valid')
                score-=1
        elif len(ans1)>=2 and ans1.endswith('D'):
            num=int(ans1[0])
            if 10>num>-1:
                l[xp][yp]=' '
                l[xm][ym]=' '
                yp+=num
                if 10>yp>-1:
                    xm=random.choice((xm-1,xm,xm+1))
                    ym=random.choice((ym-1,ym,ym+1))
                    if vis%3==0:
                        l[xm][ym]='x'
                    else:
                        l[xm][ym]=' '
                    l[xp][yp]='y'
                    near()
                    c=found()
                else:
                    yp=9
                    xm=random.choice((xm,xm-1))
                    ym=random.choice((ym,ym-1))
                    if vis%3==0:
                        l[xm][ym]='x'
                    else:
                        l[xm][ym]=' '
                    l[xp][yp]='y'
                    near()
                    c=found()
            else:
                print('Enter correct value!')
                print('Digit from 1 to 9 are valid')
                score-=1
    lans=input('Do you wnat to play again (Y/N)')
    lans.upper()
    if lans=='N':
        loop=False
        