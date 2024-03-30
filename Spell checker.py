import random
import os

dict={}
c=1
print('\t[instructions]')
print('1.File should be (.txt) only')
print('2.ref file should be (ref.txt) and added to\nwhere program file is located')
print('3.(ref.txt) file should have one word per line or\nevery word with space\n')
start=input('Do you want to start(y/n):')
start1=start.upper()
if start1=='Y':
    try:
        rfile=input('Enter reference file(.txt):')
        print()
        reffile=open(rfile,'r')
    except IOError:
        print('Reference file not found!, or maybe file is not readable')
        print('Please add reference file to where program file is located,\nname the file(ref.txt).')
        print('=======================================RESTART======================================')
    else:
        lines=reffile.readlines()
        for  rline in lines:
            rline=rline.strip()
            rline=rline.split()
            for w in rline:
                dict[w]=w
                w1=w.capitalize()
                dict[w1]=w1
        while c==1:
            rawpath=input('Enter file path(.txt):')
            try:
                file=open(rawpath,'r')
            except IOError:
                print('File not found!, or maybe file is not readable')
                print('Make sure you enter correct file path\n')
                continue
            finally:
                string=file.readline()
                if not string:
                    print('No data found!')
                    print('The file is empty!')
                    continue
                file.seek(0, 0)
                lines=file.readlines()
                len_lines=len(lines)
                tsize=0
                mis=0
                words=0
                for string in lines:
                    string1=string.split()
                    words+=len(string1)
                    tsize+=len(string)
                    for s in string1:
                        if s not in dict:
                            mis+=1
                if mis==0:
                    print('No mistakes found')
                    c=0
                    break
                print('[file status]')
                print('')
                print('size of the file:',tsize/1024,'kb')
                print('No of words:',words)
                print('NO of lines:',len_lines)
                print('No of mistakes:',mis)
                print('')
                file.seek(0,0)
                basename=os.path.basename(rawpath)
                basename1=basename.replace('.','-chk.')
                dirname=os.path.dirname(rawpath)
                newpath=dirname+'\\'+basename1
                lines=file.readlines()
                for line in lines:
                    line1=line.strip()
                    wordlist=line1.split()
                    for k in wordlist:
                        word=''
                        for l in k:
                            if l.isalnum():
                                word+=l
                        if word not in dict:
                            reflist=[]
                            for x in word:
                                t=word[:2]
                                t=t+x
                                for y in dict:
                                    if y.startswith(t):
                                        reflist.append(dict[y])
                            print('\n\t[command]\n')
                            print('O : for No replacement')
                            print('-1 : Users replacement')
                            print('1 : selected replacement\n')
                            print('=>',word,'<=')
                            loop=True
                            while loop:
                                print()
                                e=True
                                while e:
                                    try:
                                        ans=int(input('Action:'))
                                    except:
                                        continue
                                    e=False
                                if ans==1:
                                    if not reflist:
                                        print('\nNo words like [',word,'] found in Dicionary\n')
                                        continue
                                    for s in reflist:
                                        n=1
                                        print(n,'\b.'+s)
                                        n+=1
                                    s=int(input('\n\nChoose:'))
                                    line=line.replace(k,reflist[s-1])
                                    loop=False
                                elif ans==-1:
                                    rep=input('replacement:')
                                    line=line.replace(k,rep)
                                    loop=False
                                elif ans==0:
                                    print('No replacement Done')
                                    loop=False
                    newfile=open(newpath,'a')
                    newfile.write(line)
                    newfile.flush()
                print('Done checking file')
                print('File has been saved in',newpath)