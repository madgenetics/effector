f=open('pqX.sam')
out=open('filtered_pqX.sam','w')
for line in f:
    if line[0]!="@":
        try:
            if line.split('\t')[2]!='*':
                out.write(line)
        except:
            continue
f.close()
out.close()
