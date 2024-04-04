def emptylists():
    l=[]
    hl=[]
    sp=[]
    for x in range(10):
        l.append([' ',' ',' ',' ',' ',' ',' ',' ',' ',' '])
        hl.append([' ',' ',' ',' ',' ',' ',' ',' ',' ',' '])
        sp.append([' ',' ',' ',' ',' ',' ',' ',' ',' ',' '])
    return l,hl,sp

def player_pos(l,p):
    print('\t[player'+p+']')
    r='  0 1 2 3 4 5 6 7 8 9\n'
    for a in range(10):
        r+=str(a)+' '
        for b in range(10):
            r+=l[b][a]+' '
        r+='|\n'
    r+=' ===================='
    print(r)

def check_pos(x,s,l):
    s=s.split()
    n=0
    if len(s)==x:
        for a in s:
            if len(a)==3 and a[0].isdigit() and a[2].isdigit() and a[1]==',':
                n+=1
    if n==x:
        ok=False
    else:
        print('Enter correct Value!')
        ok=True
    if not ok:
        n=0
        for a in s:
            if l[int(a[0])][int(a[2])]=='0':
                n+=1
        if n!=0:
            ok=True
            print('Position already occupied!')
        else:
            ok=False
    if not ok:
        n=0
        for a in range(x):
            if a!=0:
                if s[a][0]==s[a-1][0] and s[a][2]!=s[a-1][2]:
                    n+=1
        m=0
        for a in range(x):
            if a!=0:
                if s[a][2]==s[a-1][2] and s[a][0]!=s[a-1][0]:
                    m+=1
        if n==x-1 or m==x-1:
            ok=False
        else:
            ok=True
    return ok

def test(x,l,p,sp):
    print(x)
    ok=True
    s='Enter position ship('+(x*'0')+'):'
    while ok:
        ans=input(s)
        ok=check_pos(x,ans,l)
    update_pos(ans,l,p,sp)

def enter_pos(l,p,sp):
    test(5,l,p,sp)
    test(4,l,p,sp)
    test(3,l,p,sp)
    test(2,l,p,sp)
    test(1,l,p,sp)

def action(l,hl,sp,p):
    loop=True
    while loop:
        ans=input('action:')
        loop=hit(ans,l,hl,sp,p)

def update_pos(s,l,p,sp):
    s=s.split()
    for b in s:
        l[int(b[0])][int(b[2])]='0'
    #if p=='1':
        #ship_posp1=sp
        #ship_posp1.append(s)
    #elif p=='2':
        #ship_posp2=sp
        #ship_posp2.append(s)
    
def position(p):
    l,hl,sp=emptylists()
    player_pos(l,p)
    print('Enter postion in the form of (x,y)')
    enter_pos(l,p,sp)
    player_pos(l,p)
    ans=input('Do you want to change positions again(y/n)')
    ans=ans.upper()
    if ans=='N':
        c=False
    return c,l,hl,sp

def hit(s,l,hl,sp,p):
    if len(s)==3 and s[0].isdigit() and s[2].isdigit() and s[1]==',':
        if hl[int(s[0])][int(s[2])]!='x':
            hl[int(s[0])][int(s[2])]='x'
            if l[int(s[0])][int(s[0])]=='0':
                print('Hit!')
                loop=False
                l[int(s[0])][int(s[2])]='x'
                for a in sp:
                    if s in a:
                        a.remove(s)
                    if a==[]:
                        if p==1:
                            global turnp1
                            turnp1-=1
                        if p==2:
                            global turnp2
                            turnp2-=1
            else:
                print('Missed :(')
                loop=False
        else:
            print('Invalid move! \n dont play previos moves again')
            loop=True

    else:
        print('Invalid move!')
        loop=True
    return loop

c1,c2=True,True
while c1:
    c1,lp1,hit_lp1,ship_posp1=position('1')
print('\n'*100)
while c2:
    c2,lp2,hit_lp2,ship_posp2=position('2')
turnp1,turnp2,turn=5,5,1
loop=True
while loop:
    if turnp1==0:
        print('player 2 Wins!\n gameover')
    elif turnp2==0:
        print('player 1 wins!\n gameover')
        break
    if turn==1:
        player_pos(hit_lp1,'1')
        player_pos(lp1,'1')
        for x in range(turnp1):
            action(lp2,hit_lp1,ship_posp2,1)
            next=input('player 2 ready.....')
            turn=2
    elif turn==2:
        player_pos(hit_lp2,'2')
        player_pos(lp2,'2')
        for x in range(turnp2):
            action(lp1,hit_lp2,ship_posp1,2)
            next=input('player 1 ready....')
            turn=1
