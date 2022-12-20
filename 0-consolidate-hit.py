f=open('effector-size.txt')
length={}
for line in f:
    x=line.strip('\n').strip().split('\t')
    length[x[0]]=int(x[1])
f.close()

f=open('pqXVSeffector.blast')
out=open('effector_summary_pqX.txt','w')
info={}
chro='chro'
start=0
end=0
for line in f:
    judge=0
    x=line.strip('\n').strip().split('\t')
    if x[0]!=chro:
        chro=x[0]
        start=int(x[6])
        end=int(x[7])
    else:
        if int(x[6])>=start and int(x[7])<=end:
            judge=1
        else:
            start=int(x[6])
            end=int(x[7])
    if judge==0:
        if x[1] not in info.keys():
            info[x[1]]={}
        if x[0] not in info[x[1]].keys():
            info[x[1]][x[0]]=[]
        info[x[1]][x[0]].append([x[6],x[7],x[8],x[9]])
f.close()
select={}
for i in info.keys():
    select[i]={}
    for j in info[i].keys():
        select[i][j]=[]
        if len(info[i][j])==1:
            select[i][j].append([[int(info[i][j][0][0]),int(info[i][j][0][1])],[int(info[i][j][0][2]),int(info[i][j][0][3])]])
##            print(select[i][j])
        else:
            temp=[[int(info[i][j][0][0]),int(info[i][j][0][1])],[int(info[i][j][0][1]),int(info[i][j][0][2])]]
            for k in range(1,len(info[i][j])):
                pos1=(int(info[i][j][k][0])+int(info[i][j][k][1]))/2
                if abs(pos1-(temp[0][0]+temp[0][-1])/2)<10000:
                    temp[0].append(int(info[i][j][k][0]))
                    temp[0].append(int(info[i][j][k][1]))
                    temp[1].append(int(info[i][j][k][2]))
                    temp[1].append(int(info[i][j][k][3]))
                    temp[0].sort()
                    temp[1].sort()
                else:
                    select[i][j].append(temp)
                    temp=[[int(info[i][j][k][0]),int(info[i][j][k][1])],[int(info[i][j][k][1]),int(info[i][j][k][2])]]
            if temp not in select[i][j]:
                select[i][j].append(temp)
##                print(select[i][j])
for i in select.keys():
    for j in select[i].keys():
##        print(select[i][j])
        for k in select[i][j]:
##            print(i,j,k)
            if len(k)<2:
                print(i,j,k)
            k[0].sort()
            k[1].sort()

final={}
for i in select.keys():
    final[i]={}
    for j in select[i].keys():
        final[i][j]=[]
        for k in select[i][j]:
            if abs(k[1][0]-k[1][-1])>0.7*length[i]:
                final[i][j].append([k[0][0],k[0][-1]])

for i in final.keys():
    for j in final[i].keys():
        if len(final[i][j])>0:
            result=i+'\t'+j+'\t'
            for k in final[i][j]:
                out.write(result+str(k[0])+'\t'+str(k[1])+'\n')
out.close()


                
                
            


