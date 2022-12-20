import os

good=[]

for i in os.listdir(os.getcwd()):
    if 'filtered_full_consolidate_NoMaxTarget_' in i and 'dup' not in i:
        good.append(i)


for i in good:
    f=open(i)
    out1=open('rmdup_'+i,'w')
    out2=open('duplog_'+i,'w')
    info={}
    for line in f:
        x=line.strip('\n').strip().split('\t')
        tag=str(int(int((int(x[2])+int(x[3]))/2)/100)) #100 bp region
        if x[1] not in info.keys():
            info[x[1]]={}
        if tag not in info[x[1]].keys():
            info[x[1]][tag]=[]
        info[x[1]][tag].append(line)
    f.close()
    for j in info.keys():
        for k in info[j].keys():
            if len(info[j][k])==1:
                out1.write(info[j][k][0])
            else:
                for l in info[j][k]:
                    out2.write(l)
    out1.close()
    out2.close()
            
    
