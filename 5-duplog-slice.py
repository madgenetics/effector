import os

good=[]

for i in os.listdir(os.getcwd()):
    if 'duplog_filtered_full_consolidate_NoMaxTarget_' in i:
        good.append(i)

out=open('NoMaxTarget_overlap_determine.fa','w')
pos={}
for i in good:
    f=open(i)
    tag=i.split('.')[0].split('_')[-1]
    pos[tag]={}
    for line in f:
        x=line.strip('\n').strip().split('\t')
        pos[tag][x[0]]=[x[1],x[2],x[3]]
    f.close()
    info={}
    f=open('assemble_'+tag+'.fasta')
    chro='tag'
    seq=''
    for line in f:
        if '>' in line:
            info[chro]=seq
            chro=line.strip('\n').strip()[1:]
            seq=''
        else:
            seq+=line.strip('\n').strip()
    info[chro]=seq
    info.pop('tag')
    f.close()
    for j in pos[tag].keys():
        chro=pos[tag][j][0]
        start=int(pos[tag][j][1])
        end=int(pos[tag][j][2])
        out.write('>'+tag+'pq'+j+'pq'+chro+'pq'+str(start)+'pq'+str(end)+'\n')
        out.write(info[chro][start:end+1]+'\n')
out.close()
    
    
    
