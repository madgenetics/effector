f=open('effector-size.txt')
effector=[]
good=[]

for line in f:
    x=line.strip('\n').strip().split('\t')
    effector.append(x[0])
f.close()

import os

for i in os.listdir(os.getcwd()):
    if '.sam' in i and 'filter' in i:
        good.append(i.split('.')[0])

info={}

for i in good:
    f=open(i+'.sam')
    info[i]={}
    for j in effector:
        info[i][j]=0
    for line in f:
        if line[0]!='@':
            x=line.strip('\n').strip().split('\t')
            if x[2] in info[i].keys():
                info[i][x[2]]+=1
    f.close()

out=open('filtered_sam-effector-summary.txt','w')

head='effector\t'
for i in good:
    head+=i+'\t'
out.write(head.strip('\t')+'\n')

for i in effector:
    result=i+'\t'
    for j in good:
        result+=str(info[j][i]/2)+'\t'
    out.write(result.strip('\t')+'\n')
out.close()
    
