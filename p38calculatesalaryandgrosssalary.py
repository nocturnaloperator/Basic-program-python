salary=int(input("enter salary=>"))
da=salary*0.52
ma=salary*0.1
hra=salary*0.1
va=salary*0.1
itc= salary*0.05
pf= salary*0.11
basic=8000
grosssalary=basic + da + hra + ma + itc + va
netsalary= grosssalary-pf
print("final salary=> ", netsalary)


