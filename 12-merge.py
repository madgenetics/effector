f=open('Summary_StrainBlastEffector_copyNum_NoMaxTarget.txt')
sample=[]
info={}
effector=[]
for line in f:
    x=line.strip('\n').strip().split('\t')
    for i in range(1,len(x)):
        sample.append(x[i])
    break

for i in sample:
    info[i]={}

for line in f:
    x=line.strip('\n').strip().split('\t')
    for i in range(1,len(x)):
        info[sample[i-1]][x[0]]=int(x[i])
    effector.append(x[0])
f.close()

f=open('reverseBlast-all-Effector-summary_NoMaxTarget.txt')
for line in f:
    x=line.strip('\n').strip().split('\t')
    sample2=[]
    for i in range(1,len(x)):
        sample2.append(x[i])
    break

for line in f:
    x=line.strip('\n').strip().split('\t')
    for i in range(1,len(x)):
        info[sample2[i-1]][x[0]]+=int(x[i])
f.close()

out=open('merged_NoMaxTarget_effector_copyNum.txt','w')

head='effector\t'
for i in sample:
    head+=i+'\t'
out.write(head.strip('\t')+'\n')

for i in effector:
    result=i+'\t'
    for j in sample:
        result+=str(info[j][i])+'\t'
    out.write(result.strip('\t')+'\n')
out.close()
