info={}
sample=[]
effector=[]

f=open('filtered_sam-effector-summary.txt')
sample2=[]
for line in f:
    x=line.strip('\n').strip().split('\t')
    for i in range(1,len(x)):
        sample2.append(x[i].split('_')[1])
        info[x[i].split('_')[1]]={}
    break

for line in f:
    x=line.strip('\n').strip().split('\t')
    for i in range(1,len(x)):
        if int(float(x[i]))<4:
            info[sample2[i-1]][x[0]]='N-'+str(int(float(x[i])))+'|'
        else:
            info[sample2[i-1]][x[0]]='Y-'+str(int(float(x[i])))+'|'
f.close()

f=open('merged_NoMaxTarget_effector_copyNum.txt')
for line in f:
    x=line.strip('\n').strip().split('\t')
    for i in range(1,len(x)):
        sample.append(x[i])
    break

for line in f:
    x=line.strip('\n').strip().split('\t')
    effector.append(x[0])
    for i in range(1,len(x)):
        info[sample[i-1]][x[0]]+=x[i]
f.close()



out=open('improved-merged_FilteredSam-NoMaxTarget_effector_copyNum.txt','w')

head='effector\t'
for i in sample:
    head+=i+'\t'
out.write(head.strip('\t')+'\n')
for i in effector:
    result=i+'\t'
    for j in sample:
        result+=info[j][i]+'\t'
    out.write(result.strip('\t')+'\n')
out.close()
