def answer(total_lambs):
    # your code here
    if total_lambs>2:
        most_generous=[1,2]
        least_generous=[1,1]
    else:
        return 0
    flg1=0
    flg2=0
    while 1>0:
        if sum(most_generous)+2*most_generous[-1]<=total_lambs and most_generous[-2]+most_generous[-1]<=most_generous[-1]*2:
            most_generous.append(most_generous[-1]*2)
            flg1=1
        if sum(least_generous)+least_generous[-1]+least_generous[-2]<=total_lambs and least_generous[-1]-least_generous[-2]>=0:
            least_generous.append(least_generous[-1]+least_generous[-2])
            flg2=1
        
        if flg1==0 and flg2==0:
            l=total_lambs-sum(most_generous)
            if most_generous[-1]+most_generous[-2]<=l:
                most_generous.append(l)
            return abs(len(least_generous)-len(most_generous))
        flg1=0
        flg2=0
        
        