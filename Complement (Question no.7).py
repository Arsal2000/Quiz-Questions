x=int(input("Enter the value: "))
comp=bin(x)
comp=comp.replace('0','x')
comp=comp.replace('1','0')
comp=comp.replace('x','1')
print("The first complement of",x,"is",comp[2:])
comp=comp[2:]
comp=int(comp,2)
comp=comp+1
comp=bin(comp)
comp=comp[1:]
comp=comp.replace('b','0')
print("The second complement of",x,"is",comp)

