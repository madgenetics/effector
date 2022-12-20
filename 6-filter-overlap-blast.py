info={}
f=open('NoMaxTarget_overlap_determine.blast')
used={}
for line in f:
    x=line.strip('\n').split('\t')
    if x[0] not in used.keys():
        used[x[0]]=1
        y=x[0].split('pq')
        if y[1]==x[1]:
            info[x[0]]=1
f.close()

import os

good=[]

for i in os.listdir(os.getcwd()):
    if 'rmdup_filtered' in i:
        good.append(i)


for i in good:
    f=open(i)
    out=open('reverseBlast-final_result_NoMaxTarget_'+i.split('_')[-1],'w')
    for line in f:
        out.write(line)
    f.close()
    try:
        f=open('duplog_filtered_full_consolidate_NoMaxTarget_'+i.split('_')[-1])
        for line in f:
            x=line.strip('\n').strip().split('\t')
            tag=i.split('.')[0].split('_')[-1]+'pq'+x[0]+'pq'+x[1]+'pq'+x[2]+'pq'+x[3]
            if tag in info.keys():
                out.write(line)
    except:
        print(i)
    out.close()
            
