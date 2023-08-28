n=int(input('how many data points:'))
a=[]
b=[]
for i in range(1,n+2):
  print(f"enter value of x {i}:", end="")
  s=float(input())
  a.append(s)
  print(f"enter value of y {i}:", end="")
  r=float(input())
  b.append(r)
print('*'*30)  

def poly(x,n,a,b):
  c=0
  for i in range(0,n+1):
    d=1
    for j in range(0,n+1):
      if j!=i:
        d*=(x-a[j])/(a[i]-a[j])
    c+=b[i]*d 
  return c
  
x=float(input('enter value of x for which y is required:'))

print('corresponding y is',poly(x,n,a,b))