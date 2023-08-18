print(max([1,["a"]],[4,["b"]],[10,['a','b']]))
print([1,["a"]]+[4,["b"]]+[10,['a']])
line=input()
line2=input()
#line = line.strip()  
def remp_vir(line):  
   line=line.replace('\t',',')
   line=line.replace('|',',')
   return line
datas= line.split(',')
       #  datas= line.split(',')
print(remp_vir(line))
print(remp_vir(line2))