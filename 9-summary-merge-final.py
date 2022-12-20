info={}
f=open('effector-size.txt')
effector=[]
for line in f:
    x=line.strip('\n').strip().split('\t')
    info[x[0]]={}
    effector.append(x[0])
f.close()

sample=[]

import os

good=[]

for i in os.listdir(os.getcwd()):
    if 'effector_summary_' in i:
        good.append(i)


for i in good:
    f=open(i)
    strain=i.split('_')[-1].split('.')[0]
    sample.append(strain)
    for j in info.keys():
        info[j][strain]=0
    for line in f:
        x=line.strip('\n').strip().split('\t')[0]
        info[x][strain]+=1
    f.close()

f=open('reverseBlast-all-Effector-summary_NoMaxTarget.txt')
sample2=[]
for line in f:
    x=line.strip('\n').strip().split('\t')
    for i in range(1,len(x)):
        sample2.append(x[i])
    break

for line in f:
    x=line.strip('\n').strip().split('\t')
    for i in range(1,len(x)):
        info[x[0]][sample2[i-1]]+=1

out=open('Summary_effector_copyNum_final_NoMaxTarget.txt','w')
head='effector\t'
for i in sample:
    head+=i+'\t'
out.write(head.strip('\t')+'\n')

for i in effector:
    result=i+'\t'
    for j in sample:
        result+=str(info[i][j])+'\t'
    out.write(result.strip('\t')+'\n')
out.close()
    
