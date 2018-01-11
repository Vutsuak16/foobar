def answer(n):
    
    n=int(n)
    sol={1:0,2:1}
    
    def support(x):
        
        if x in sol:
            return sol[x]
        
        if x%2 != 0:
            sol[x]=min(support((x+1)/2)+2,support((x-1)/2)+2)
        else:
            sol[x]=support(x/2)+1
        
        return sol[x]
    
    return support(n)
            
    
   