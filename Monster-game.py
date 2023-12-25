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
        ans2=input('do you want to play again(y/n):')
        if ans2=='y' or ans2=='Y':
            l=['x',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            score=0
            m,p=0,0
            ans=False
            x,y=0,9
            return l,score,m,p,x,y
        elif ans2=='n' or ans2=='N':
            c=0
            return c
        else:
            ans=True
    

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
    
def start():
    print('[x] - monster\n[y] - player')
    print('')
    
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
                    l,score,m,p=exit()
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
                    l,score,m,p,x,y=exit()
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
                    l,score,m,p,x,y=exit()
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
                    l,score,m,p,x,y=exit()
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
                    l,score,m,p,x,y=exit()
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
                    l,score,m,p,x,y=exit()
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
            l,score,m,p,x,y=exit()
    else:
        print('please enter a correct value')
        score-=1


        