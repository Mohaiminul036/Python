str1= "ABCCCB"
lst1=list(str1)
counts={}
for i in lst1:
    counts[i]=counts.get(i,0)+1
lst2=list(counts.items())
lst2.sort(key=lambda x:x[1],reverse=True)
for j in range(len(lst2)):
    print("{}出现{}次".format(lst2[j][0],lst2[j][1]))


x,y="x","y"
x,y=y,x
print(x,y)

numbers=1,2,3
print(numbers)
a,b,c=numbers
print(a,b,c)

d,e,f=[4,5,6]
print(d,e,f)

j,k,l=b'\x00\x13\x34'
print(j,k,l)

x,y,*rest=[1,2,3,4,5,66]

a="Long Pu JUn CQust".split()
first,*mi,last=a
print(first,mi,last)


import this

