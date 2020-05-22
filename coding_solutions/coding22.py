def missNo(x):
    l=len(x)
    maxs=max(x)
    mins=min(x)
    for i in range(0,l):
        if mins not in x and mins<=maxs:
            return mins
        else:
            mins+=1
            
y=[9,8,7,6,5,3]
m=(missNo(y))
print("missing number is",m)