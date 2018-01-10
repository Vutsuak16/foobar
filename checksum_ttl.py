def answer(start, length):
    # your code here
    
    
    
    xor=[]
    for i in xrange(length):
        l=[j for j in xrange(start,length+start-i)]
        xor.append(reduce(lambda x,y:x^y,l))
        start+=length
        del l
    return reduce(lambda x,y:x^y,xor)
            