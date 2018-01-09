def start(s):
	maxi=1
	for i in range(1,len(s)):
		k=s.split(s[:i])
		if k[0] == '' and len(k)-1>maxi and len(set(k))==1:
			maxi=len(k)-1
	return maxi	 
