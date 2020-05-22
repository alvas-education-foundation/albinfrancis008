#Find the number that is missing from the array containing n distinct numbers taken from 0,1,2...n
def missNo(x):
    l=len(x)
    maxs=max(x)
    mins=min(x)
    for i in range(0,l):
        if mins not in x and mins<=maxs:
            return mins
        else:
            mins+=1
            
y=[20,19,18,17,16,15,13]
m=(missNo(y))
print("missing number is",m)
