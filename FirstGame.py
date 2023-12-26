def menu():
    print("")
    print('[Game menu]')
    print('1.Random game')
    print('2.Guess the number')
    print('3.Die throw')
    print('4.Stone,paper,scissors')
    print('5.Coin toss')
    print('6.monster game')
    print("7.help")
    print('8.exit')
    
def end():
    con=input('(Press and key to continue)')
    menu()

def coincheck():
    if coinsentered<=Balance:
        ck=False
        return ck
    else:
        print('Not enough coins (your balance:',Balance,')')
        ck=True
        return ck
        
import random
print('do you want to start(Y/N)')
ck=True                
while True:
    ans=input(":")
    ans1=ans.upper()
    if ans1=="N":
        break
    elif ans1=='Y':
        Balance=1000
        points=Balance-1000
        print('You are given 1000 coins')
        menu()  
        while True:
            rbonus=random.randint(1,100)
            b1=random.randint(1,10)
            b2=random.randint(1,10)
            b3=random.randint(1,10)
            if rbonus==1:
                print('============BONUS===========')
                print('you won a bonus of 2000 coins')
                Balance+=2000
                end()
                continue
            elif rbonus==100:
                rb1=b1*100
                rb2=b2*10
                rb3=b3
                rsum=rb1+rb2+rb3
                print('you got a gift :)')
                rans=input('(Enter any key to accept)')
                print('')
                print('you got',rsum,'coins')
                Balance+=rsum
                end()
                continue
            if Balance==0:
                print('Game over :/ you lose')
                print('restart the game to play again')
                break
            gamemenu=input(':')
            if gamemenu=='1':
                print('The computer will generate a number between 1 to 10')
                print('if the number generated matches the number you enter')
                print('then the coins entered will increase by 300%.')
                print('')
                while ck:
                    coinsentered=int(input('enter coins:'))
                    ck=coincheck()
                enternum=int(input('Enter num between 1 to 10:'))
                comnum=random.randint(1,10)
                if enternum!=comnum:
                    print('you lose :/ \n the number was',comnum)
                    Balance-=coinsentered
                    end()
                    continue
                if enternum==comnum:
                    print('congratulations! you won 300% of your entered coins')
                    coinsentered*=3
                    Balance+=coinsentered
                    end()
                    continue
            elif gamemenu=='2':
                print('')
                print('The computer will generate a num between 1 to 100')
                print('if the num generated matches the num you enter')
                print('then the coinsenetered will increase by 500%.')
                print('you will get 5 attempts to guess')
                print('')
                while ck:
                    coinsentered=int(input('enter coins:'))
                    ck=coincheck()
                randomnum=random.randint(1,100)
                guessnum=int(input('enter num between 1 to 100:'))
                if guessnum!=randomnum:
                    if guessnum<randomnum:
                        print('your guess is too low')
                    else:
                        print('your guess is too high' )
                else:
                    print('congratulation! you won')
                    coinsentered*=5
                    Balance+=coinsentered
                    end()
                    continue
                guessnum2=int(input('enter num between 1 to 100:'))
                if guessnum2!=randomnum:
                    if guessnum2<randomnum:
                        print('your guess is too low')
                    else:
                        print('your guess is too high' )
                else:
                    print('congratulation! you won')
                    coinsentered*=5
                    Balance+=coinsentered
                    end()
                    continue
                guessnum3=int(input('enter num between 1 to 100:'))
                if guessnum3!=randomnum:
                    if guessnum3<randomnum:
                        print('your guess is too low')
                    else:
                        print('your guess is too high' )
                else:
                    print('congratulation! you won')
                    coinsentered*=5
                    Balance+=coinsentered
                    end()
                    continue
                guessnum4=int(input('enter num between 1 to 100:'))
                if guessnum4!=randomnum:
                    if guessnum4<randomnum:
                        print('your guess is too low')
                    else:
                        print('your guess is too high' )
                else:
                    print('congratulation! you won')
                    coinsentered*=5
                    Balance+=coinsentered
                    end()
                    continue
                guessnum5=int(input('enter num between 1 to 100:'))
                if guessnum5!=randomnum:
                    print('you lose \n The number was',randomnum)
                    Balance-=coinsentered
                    end()
                    continue
                elif guessnum==randomnum:
                    print('congratulations! you won')
                    coinsentered*=5
                    Balance+=coinsentered
                    end()
                    continue
            elif gamemenu=='3':
                print('The computer will generate a number between')
                print('1 to 6 three times and sum of three num matches')
                print('the number you enter then the entered coins will')
                print('increase by 1000%.')
                print('')
                while ck:
                    coinsentered=int(input('enter coins:'))
                    ck=coincheck()
                enternum=int(input("Enter number:"))
                a=random.randint(1,6)
                gen=input('enter any key to generate:')
                if bool(gen) or bool(1):
                    print('throw1:',a)
                b=random.randint(1,6)
                gen2=input('enter any key to generate:')
                if bool(gen2) or bool(1):
                    print('throw2:',b)
                c=random.randint(1,6)
                gen3=input('enter any key to generate:')
                if bool(gen3) or bool(1):
                    print('throw3:',c)
                sum1=a+b+c
                if sum1!=enternum:
                    print('you lose\n The number was',sum1)
                    Balance-=coinsentered
                    end()
                    continue
                else:
                    print('congratulations! you won')
                    coinsentered*=10
                    Balance+=coinsentered
                    end()
                    continue
            elif gamemenu=='4':
                print('The computer will randomly select between stone,')
                print('paper and scissors, if you lose then the coinsentered')
                print("will be subtracted from your balance and if you")
                print('win then the coinsentered will increase by 500%.')
                print('')
                while ck:
                    coinsentered=int(input('enter coins:'))
                    ck=coincheck() 
                com=int(random.randint(1,3))
                if com==1:
                    gcom='stone'
                elif com==2:
                    gcom='paper'
                elif com==3:
                    gcom='scissors'
                print('computer has selected')
                print('')
                user=int(input('enter(1=stone,2=paper,3=scissors):'))
                if user==1:
                    guser='stone'
                elif user==2:
                    guser='paper'
                elif user==3:
                    guser='scissors'
                if com==user:
                    print('you played(',guser,')')
                    print('computer played(',gcom,')')
                    print('it is a (draw)')
                    end()
                    continue
                elif com<user<3:
                    print('you played(',guser,')')
                    print('computer played(',gcom,')')
                    print('you won')
                    coinsentered*=3
                    Balance+=coinsentered
                    end()
                    continue
                elif com<2<user:
                    print('you played(',guser,')')
                    print('computer played(',gcom,')')
                    print('you lose')
                    Balance-=coinsentered
                    end()
                    continue
                elif 3>com>user:
                    print('you played(',guser,')')
                    print('computer played(',gcom,')')
                    print('you lose')
                    Balance-=coinsentered
                    end()
                    continue
                elif 1<com<user:
                    print('you played(',guser,')')
                    print('computer played(',gcom,')')
                    print('you won')
                    coinsentered*=3
                    Balance+=coinsentered
                    end()
                    continue
                elif com>2>user:
                    print('you played(',guser,')')
                    print('computer played(',gcom,')')
                    print('you won')
                    coinsentered*=3
                    Balance+=coinsentered
                    end()
                    continue
                elif com>user>1:
                    print('you played(',guser,')')
                    print('computer played(',gcom,')')
                    print('you lose')
                    Balance-=coinsentered
                    end()
                    continue
            elif gamemenu=='5':
                print('IF YOU GET 3 HEADS YOU WIN')
                print('')
                while ck:
                    coinsentered=int(input('enter coins:'))
                    ck=coincheck()
                coin1=random.randint(1,2)
                print('')
                cans1=input('enter any key to fip a coin:')
                if bool(cans1) or bool(1):
                    if coin1==1:
                        tcoin1='heads'
                        print('Toss1:',tcoin1)
                    elif coin1==2:
                        tcoin1='tails'
                        print('Toss1:',tcoin1)
                coin2=random.randint(1,2)
                cans2=input('enter any key to fip a coin:')
                if bool(cans2) or bool(1):
                    if coin2==1:
                        tcoin2='heads'
                        print('Toss2:',tcoin2)
                    elif coin2==2:
                        tcoin2='tails'
                        print('Toss2:',tcoin2)
                coin3=random.randint(1,2)
                cans3=input('enter any key to fip a coin:')
                if bool(cans3) or bool(1):
                    if coin3==1:
                        tcoin3='Heads'
                        print('Toss3:',tcoin3)
                    elif coin3==2:
                        tcoin3='tails'
                        print('Toss3:',tcoin3)
                if coin1==coin2==coin3==1:
                    print('Jackpot! you got 3 heads')
                    print('you won')
                    coinsentered*=5
                    Balance+=coinsentered
                    end()
                    continue
                else:
                    print('you lose :/')
                    Balance-=coinsentered
                    end()
                    continue
            elif gamemenu=='bal':
                print('your balance=',Balance)
                end()
                continue
            elif gamemenu=='points':
                print('your points:', points)
                end()
                continue
            elif gamemenu=='check profile':
                print('profile')
                print("")
                try:
                    print('name:',name)
                except NameError:
                    print('There is no active profile\nType (new profile) to create a profile')
                    continue
                print('balance:',Balance)
                print('points:',points)
                end()
                continue
            elif gamemenu=='new profile':
                print('[profile]')
                print("")
                name=input('entername:')
                print('profile created')
                print('name:',name)
                print('balance:',Balance)
                print('points:',points)
                end()
                continue
            elif gamemenu=='save':
                profile=open('profile1','w')
                profile.write(name)
                profile.write('\n')
                b1=str(Balance)
                profile.write(b1)
                profile.write('\n')
                p1=str(points)
                profile.write(p1)
                profile.close()
                print('profile save in profile 1')
                end()
                continue
            elif gamemenu=='add profile':
                aprofile=input('profile name:')
                profile1=open(aprofile,'r')
                n=profile1.readlines()
                name=n[0]
                Balance=n[1]
                points=n[2]
                print('profile added')
                end()
                continue
            elif gamemenu=='reset':
                name='None(create a new profile)'
                Balance=1000
                points=Balance-1000
                print('name:',name)
                print('balance:',Balance)
                print('points:',points)
                print('your profile has been reset')
                print('create a new profile')
                end()
                continue
            elif gamemenu=='8':
                print('Are you sure you want to exit(Y/N)')
                exitans=input(':')
                exitans1=exitans.upper()
                if exitans1=='Y':
                    c-=1
                    print('============Restart============')
                    break
                elif exitans=='N':
                    end()
            elif gamemenu=='7':
                print('Help menu')
                print('')
                print('1.How to play')
                print('2.All commands')
                print('3.exit')
                while True:
                    helpmenu=input(':')
                    if helpmenu=='1':
                        print('')
                        print('how to play')
                        print('''
    The program has 5 games(Random game, guess the number, die throw,stone paper and scissors, coin toss)
    In the beginning, you are given 1000 coins and to earn more coins you need to play and win the game, 
    if you lose then the coins you enter will be subtracted from your balance and if you win then the coins
    you enter will increase by some percent and will get added to your balance.
    (type (bal) to check balance)
    ''')
                        print('')
                        print('''
    Random game: The computer will generate a number between 1 to 10, if the number generated matches the number 
    you enter(guess) then the coinsentered will increase by 300%.
    ''')
                        print('')
                        print('''
    Guess the number: The computer will generated a number between 1 to 100, if the number generated matches the
    number you enter then the coins you enter will increase by 500%, you will get 5 attempts to guess the number
    ''')
                        print('')
                        print('''
    Die throw: The computer will generate a number between 1 to 6 three times and sum of three numbers matches
    the number you enter then the coins you enter will increse by 1000%.
    ''')
                        print('')
                        print('''
    Coin toss: IF YOU GET THREE HEAD IN A ROW YOU WIN.                          
    ''')
                        continue
                    elif helpmenu=='2':
                        print('''
    All commands

    bal - to show Balance
    new profile - to add profile
    add profile - to add an external profile
    check profile - to check profile
    reset - to reset profile
    save - to save balance and points and profile
    points - to show points
    ''')
                        continue
                    elif helpmenu=='3':
                        end()
                        break
            elif gamemenu=='6':
                def result():
                    result='|'
                    for x in range (0,10):
                        result+=l[x]+'.'
                    result+='|'
                    return result
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
                    global Balance,z
                    z=0
                    Balance+=score*10
                    
                def start():
                    print('[x] - monster\n[y] - player')
                    print('For each turn you survive your score increases by 1')
                    print('1 score = 10 coins')
                    
                x,y=0,9
                monster=0
                z=1
                m=0
                p=0
                score=0
                l=['x',' ',' ',' ',' ',' ',' ',' ',' ',' ']
                start()
                while z==1:
                    score+=z
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
                                    print('monster is near you!')
                                    monster=1
                                elif abs(m-p)==0:
                                    lose()
                                    end()
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
                                    print('monster is near you!')
                                    monster=1
                                elif abs(m-p)==0:
                                    lose()
                                    end()
                        else:
                            ans1=0
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
                                    print('monster is near you!')
                                    monster=1
                                elif abs(m-p)==0:
                                    lose()
                                    end()
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
                                    print('monster is near you')
                                    monster=1
                                elif abs(m-p)==0:
                                    lose()
                                    end()
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
                                    print('monster is near you')
                                    monster=1
                                elif abs(m-p)==0:
                                    lose()
                                    end()
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
                                    print('monster is near you')
                                    monster=1
                                elif abs(m-p)==0:
                                    lose()
                                    end()
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
                            end()
                    else:
                        print('please enter a correct value')
                        score-=1


        
                    
                    
                
                    
            
                
                    
                    
                        
                        
                        
                    
                          
                        
                              
                                  

                            
