def average(start,end):
    s=0
    c=0
    for i in range(start,end+1):#1,2,3,4,5
        s=s+i #0+1=1+2=3+3=6+4=10+5=15
        c=c+1 #5 
    print("average:",s/c) #15/5
        
        
def even(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
    
    
def duplicates(li):
    d=[]#12,34,56,78,23
    for i in li:#12,34,56,78,23,12,12,12,23
        if i not in d:
            d.append(i)
    print(d)
    
    
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact


def leapyears(l,u):
    for i in range(l,u+1):
        if i%400==0 or (i%100!=0 and i%4==0):
            print(i,end=" ")