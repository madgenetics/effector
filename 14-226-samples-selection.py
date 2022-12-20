f=open('226-sample-list.txt')
sample=[]
for line in f:
    sample.append(line.strip('\n').strip())
print(sample)
f.close()

f=open('improved-merged_FilteredSam-NoMaxTarget_effector_copyNum.txt')
out=open('226-improved-merged_FilteredSam-NoMaxTarget_effector_copyNum.txt','w')
pos=[0]

for line in f:
    x=line.strip('\n').strip().split('\t')
    for i in sample:
        for j in range(len(x)):
            if x[j]==i:
                pos.append(j)
    result=''
    for i in pos:
        result+=x[i]+'\t'
    out.write(result+'Y_num\n')
    break

for line in f:
    x=line.strip('\n').strip().split('\t')
    result=''
    count=0
    for i in pos:
        if 'Y' in x[i]:
            count+=1
        result+=x[i]+'\t'
    out.write(result+str(count)+'\n')
out.close()
f.close()
        

