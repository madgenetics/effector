import os

good=[]
sample=[]
for i in os.listdir(os.getcwd()):
    if 'reverseBlast-final_result_NoMaxTarget_' in i:
        good.append(i)
        sample.append(i.split('.')[0].split('_')[-1])

info={}

f=open('effector-size.txt')
for line in f:
    x=line.strip('\n').strip().split('\t')
    info[x[0]]={}
    for i in sample:
        info[x[0]][i]=0
f.close()
##print(info)

for i in good:
    f=open(i)
    strain=i.split('.')[0].split('_')[-1]
    for line in f:
        x=line.split('\t')[0]
        info[x][strain]+=1
    f.close()

out1=open('reverseBlast-all-Effector-summary_NoMaxTarget.txt','w')
##out2=open('Known-Effector-summary.txt','w')
##out3=open('Unknown-Effector-summary.txt','w')
head='Effector\t'
for i in sample:
    head+=i+'\t'
out1.write(head.strip('\t')+'\n')
##out2.write(head.strip('\t')+'\n')
##out3.write(head.strip('\t')+'\n')
for i in info.keys():
    result=i+'\t'
    for j in sample:
        result+=str(info[i][j])+'\t'
    out1.write(result.strip('\t')+'\n')
out1.close()
    
    
