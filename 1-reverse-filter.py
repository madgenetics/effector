##f=open('effector-size.txt')
##length={}
##for line in f:
##    x=line.strip('\n').strip().split('\t')
##    length[x[0]]=int(x[1])
##f.close()


f=open('effector_summary_pqX.txt')
hit={}
for line in f:
    x=line.strip('\n').strip().split('\t')
    if x[1] not in hit.keys():
        hit[x[1]]={}
        hit[x[1]]['pos']=[]
    start=max(0,int(x[2])-1000)
    end=int(x[3])+1000
    hit[x[1]][str(start)]=end
    hit[x[1]]['pos'].append(start)
f.close()

for i in hit.keys():
    hit[i]['pos'].sort()

f=open('effectorVSpqX.blast')
out=open('NoMaxTarget_filtered_reverseBlast_effectorVSpqX.blast','w')

for line in f:
    x=line.strip('\n').strip().split('\t')
    if x[1] not in hit.keys():
        out.write(line)
    else:
        start=int(x[8])
        judge=0
        for i in hit[x[1]]['pos']:
            if start>=i and start<=hit[x[1]][str(i)]:
                judge=1
        if judge==0:
            out.write(line)
f.close()
out.close()

