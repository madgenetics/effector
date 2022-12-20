import os

good=[]

gene={}
f=open('effector-size.txt')
for line in f:
    x=line.strip('\n').strip().split('\t')
    gene[x[0]]=x[1]
f.close()


for i in os.listdir(os.getcwd()):
    if 'NoMaxTarget_filtered_reverseBlast_effector' in i:
        good.append(i)

for i in good:
    f=open(i)
    out=open('full_consolidate_NoMaxTarget_'+i.split('.')[0].split('_')[-1]+'.txt','w')
    info={}
    for line in f:
        x=line.split('\t')
        if x[0] not in info.keys():
            info[x[0]]={}
        if x[1] not in info[x[0]].keys():
            info[x[0]][x[1]]={}
            info[x[0]][x[1]]['pos']=[]
        start=min(int(x[8]),int(x[9]))
        end=max(int(x[8]),int(x[9]))
        query_start=min(int(x[6]),int(x[7]))
        query_end=max(int(x[6]),int(x[7]))
        info[x[0]][x[1]]['pos'].append(start)
        info[x[0]][x[1]][str(start)]=[end,query_start,query_end]
    f.close()
    for j in info.keys():
        for k in info[j].keys():
            info[j][k]['pos'].sort()
    for j in info.keys():
        for k in info[j].keys():
            if len(info[j][k]['pos'])==1:
                out.write(j+'\t'+k+'\t'+str(info[j][k]['pos'][0])+'\t'+str(info[j][k][str(info[j][k]['pos'][0])][0])+'\t'+str(info[j][k][str(info[j][k]['pos'][0])][1])+'\t'+str(info[j][k][str(info[j][k]['pos'][0])][2])+'\t'+gene[j]+'\n')
            else:
                start=info[j][k]['pos'][0]
                end=info[j][k][str(start)][0]
                query_start=info[j][k][str(start)][1]
                query_end=info[j][k][str(start)][2]
                result=[]
                temp=[start,end]
                query_temp=[query_start,query_end]
                query_result=[]
                for l in range(1,len(info[j][k]['pos'])):
                    start2=info[j][k]['pos'][l]
                    end2=info[j][k][str(start2)][0]
                    if abs(start2-temp[-1])<=5000:
                        temp.append(start2)
                        temp.append(end2)
                        query_temp.append(info[j][k][str(start2)][1])
                        query_temp.append(info[j][k][str(start2)][2])
                    else:
                        result.append(temp)
                        query_result.append(query_temp)
                        temp=[start2,end2]
                        query_temp=[info[j][k][str(start2)][1],info[j][k][str(start2)][2]]
                if temp not in result:
                    result.append(temp)
                    query_result.append(query_temp)
                for l in query_result:
                    l.sort()
                for l in range(len(result)):
                    y=result[l]
                    z=query_result[l]
                    out.write(j+'\t'+k+'\t'+str(y[0])+'\t'+str(y[-1])+'\t'+str(z[0])+'\t'+str(z[-1])+'\t'+gene[j]+'\n')
    out.close()
                
    
