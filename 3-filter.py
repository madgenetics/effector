import os

good=[]

for i in os.listdir(os.getcwd()):
    if 'full_consolidate_NoMaxTarget_' in i and 'filtered' not in i:
        good.append(i)

for i in good:
    f=open(i)
    out=open('filtered_'+i,'w')
    for line in f:
        x=line.strip('\n').strip().split('\t')
        perc=100*abs(int(x[4])-int(x[5]))/int(x[6])
        if perc>=50: #50% length must get hit
            out.write(line)
    f.close()
    out.close()
