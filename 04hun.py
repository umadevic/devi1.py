k=int(input())
l1=input(" ")
l1=list(l1.split(' '))
u={}
for i in l1:
   if i in u:
      u[i]+=1
   else:
      u[i]=1
for key,value in u.items():
  if value==1:
     print(key)
