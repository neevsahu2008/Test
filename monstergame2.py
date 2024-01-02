import random

def result():
    result='|'
    for x in range (0,10):
        result+=l[x]+'.'
    result+='|'
    return result

def exit():
    ans=True
    while ans:
        print('To play again type [A]')
        print('To Start a new game type [N]')
        print('To exit type [E]')
        ans2=input(':').upper()
        if ans2=='A':
            l=['x',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            score=0
            m,p=0,0
            ans=False
            x,y=0,9
            c=1
            leave=True
            print('')
            return l,score,m,p,x,y,c,leave
        elif ans2=='N':
            l=['x',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            score=0
            m,p=0,0
            ans=False
            x,y=0,9
            c=0
            leave=True
            print('')
            return l,score,m,p,x,y,c,leave
        elif ans2=='E':
            l=['x',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            score=0
            m,p=0,0
            ans=False
            x,y=0,9
            c=0
            leave=False
            print('')
            return l,score,m,p,x,y,c,leave

def monster_near():
    if (p-3)>-1:
        x=p-3
    else:
        x=0
    if (p+3)<10:
        y=p+3
    else:
        y=9
    return x,y

def lose():
    print('You were Caught!')
    print('You lose :(')
    print('')
    print('Your score:',score)

def win():
    print('You got him!')
    print('You won!')
    
def start():
    print('[x] - Monster\n[y] - Player')
    print('')

def start2():
    print('[x] - Player\n[y] - Monster')
    print('')

leave=True
begin=True
print('Do you want to start(y/n)')
if begin:
    ans2=input(':').upper()
    if ans2=='N':
        begin=False
    elif ans2=='Y':
        while leave:
            print('')
            print('[CHOOSE]')
            print('1.Play as (Human)')
            print('2.Play as (Monster)')
            print('3.Exit')
            choose=input(':')
            if choose=='1':
                x,y=0,9
                monster=0
                c=1
                m=0
                p=0
                score=0
                l=['x',' ',' ',' ',' ',' ',' ',' ',' ',' ']
                start()
                while c==1:
                    score+=c
                    r=result()
                    ans=input(r)
                    ans1=ans.upper()
                    if len(ans1)==2 and ans1.endswith('L'):
                        ans1=int(ans1[0])
                        if 10>ans1>-1:
                            l[m]=' '
                            l[p]=' '
                            p-=ans1
                            if 10>p>-1:
                                x,y=0,9
                                if monster==1:
                                    x,y=monster_near()
                                    monster=0
                                m=int(random.randint(x,y))
                                l[m]='x'
                                l[p]='y'
                                if abs(m-p)==2 or abs(m-p)==1:
                                    print('montser is near you!')
                                    monster=1
                                elif abs(m-p)==0:
                                    lose()
                                    l,score,m,p,x,y,c,leave=exit()
                            else:
                                p=0
                                x,y=0,9
                                if monster==1:
                                    x,y=monster_near()
                                    monster=0
                                m=int(random.randint(x,y))
                                l[m]='x'
                                l[p]='y'
                                if abs(m-p)==2 or abs(m-p)==1:
                                    print('montser is near you!')
                                    monster=1
                                elif abs(m-p)==0:
                                    lose()
                                    l,score,m,p,x,y,c,leave=exit()
                        else:
                            ans1=0
                            l[m]=' '
                            l[p]=' '
                            p=ans1
                            if 10>p>-1:
                                x,y=0,9
                                if monster==1:
                                    x,y=monster_near()
                                    onster=0
                                m=int(random.randint(x,y))
                                l[m]='x'
                                l[p]='y'
                                if abs(m-p)==2 or abs(m-p)==1:
                                    print('montser is near you!')
                                    monster=1
                                elif abs(m-p)==0:
                                    lose()
                                    l,score,m,p,x,y,c,leave=exit()
                    elif len(ans1)==2 and ans1.endswith('R'):
                        ans1=int(ans1[0])
                        if 10>ans1>-1:
                            l[m]=' '
                            l[p]=' '
                            p+=ans1
                            if 10>p>-1:
                                x,y=0,9
                                if monster==1:
                                    x,y=monster_near()
                                    monster=0
                                m=int(random.randint(x,y))
                                l[m]='x'
                                l[p]='y'
                                if abs(m-p)==2 or abs(m-p)==1:
                                    print('montser is near you')
                                    monster=1
                                elif abs(m-p)==0:
                                    lose()
                                    l,score,m,p,x,y,c,leave=exit()
                            else:
                                p=9
                                x,y=0,9
                                if monster==1:
                                    x,y=monster_near()
                                    monster=0
                                m=int(random.randint(x,y))
                                l[m]='x'
                                l[p]='y'
                                if abs(m-p)==2 or abs(m-p)==1:
                                    print('montser is near you')
                                    monster=1
                                elif abs(m-p)==0:
                                    lose()
                                    l,score,m,p,x,y,c,leave=exit()
                        else:
                            ans1=9
                            l[m]=' '
                            l[p]=' '
                            p=ans1
                            if 10>p>-1:
                                x,y=0,9
                                if monster==1:
                                    x,y=monster_near()
                                    monster=0
                                m=int(random.randint(x,y))
                                l[m]='x'
                                l[p]='y'
                                if abs(m-p)==2 or abs(m-p)==1:
                                    print('montser is near you')
                                    monster=1
                                elif abs(m-p)==0:
                                    lose()
                                    l,score,m,p,x,y,c,leave=exit()
                    elif len(ans)==1 and ans=='0':
                        x,y=0,9
                        l[m]=' '
                        l[p]='y'
                        if monster==1:
                            x,y=monster_near()
                            monster=0
                        m=int(random.randint(x,y))
                        l[m]='x'
                        if abs(m-p)==2 or abs(m-p)==1:
                            print('monster is near you')
                            monster=1
                        elif abs(m-p)==0:
                            lose()
                            l,score,m,p,x,y,c,leave=exit()
                    else:
                        print('please enter a correct value')
                        score-=1
            elif choose=='2':
                x,y=0,9
                c=1
                m=0
                p=0
                score=0
                l=['x',' ',' ',' ',' ',' ',' ',' ',' ',' ']
                start2()
                print('Catch the Monster!')
                while c==1:
                    score+=c
                    r=result()
                    ans=input(r)
                    ans1=ans.upper()
                    if len(ans1)==2 and ans1.endswith('L'):
                        ans1=int(ans1[0])
                        if 10>ans1>-1:
                            l[m]=' '
                            l[p]=' '
                            p-=ans1
                            if 10>p>-1:
                                x,y=0,9
                                m=int(random.randint(x,y))
                                l[m]='y'
                                l[p]='x'
                                if abs(m-p)==0:
                                    win()
                                    l,score,m,p,x,y,c,leave=exit()
                            else:
                                p=0
                                x,y=0,9
                                m=int(random.randint(x,y))
                                l[m]='y'
                                l[p]='x'
                                if abs(m-p)==0:
                                    win()
                                    l,score,m,p,x,y,c,leave=exit()
                        else:
                            ans1=0
                            l[m]=' '
                            l[p]=' '
                            p=ans1
                            if 10>p>-1:
                                x,y=0,9
                                m=int(random.randint(x,y))
                                l[m]='y'
                                l[p]='x'
                                if abs(m-p)==0:
                                    win()
                                    l,score,m,p,x,y,c,leave=exit()
                    elif len(ans1)==2 and ans1.endswith('R'):
                        ans1=int(ans1[0])
                        if 10>ans1>-1:
                            l[m]=' '
                            l[p]=' '
                            p+=ans1
                            if 10>p>-1:
                                x,y=0,9
                                m=int(random.randint(x,y))
                                l[m]='y'
                                l[p]='x'
                                if abs(m-p)==0:
                                    win()
                                    l,score,m,p,x,y,c,leave=exit()
                            else:
                                p=9
                                x,y=0,9
                                m=int(random.randint(x,y))
                                l[m]='y'
                                l[p]='x'
                                if abs(m-p)==0:
                                    win()
                                    l,score,m,p,x,y,c,leave=exit()
                        else:
                            ans1=9
                            l[m]=' '
                            l[p]=' '
                            p=ans1
                            if 10>p>-1:
                                x,y=0,9
                                m=int(random.randint(x,y))
                                l[m]='y'
                                l[p]='x'
                                if abs(m-p)==0:
                                    win()
                                    l,score,m,p,x,y,c,leave=exit()
                    elif len(ans)==1 and ans=='0':
                        x,y=0,9
                        l[m]=' '
                        l[p]='x'
                        m=int(random.randint(x,y))
                        l[m]='y'
                        if abs(m-p)==0:
                            win()
                            l,score,m,p,x,y,c,leave=exit()
                    else:
                        print('please enter a correct value')
                        score-=1
            elif choose=='3':
                leave=False