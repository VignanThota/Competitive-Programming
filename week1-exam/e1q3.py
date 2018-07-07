def couples(row,count):
	n=len(row)
	couple=[None]*n
	for i, j in enumerate(row):
		couple[j]=i
	c=0
	for i in range(0,n,2):
		p,z=row[i:i+2]
		q=p-1 if p%2 else p+1
		if q!=z:
			j=couple[q]
			row[j]= z
			couple[z]=j
			c+=1
	if(c==count):
		print("True")
	else:
		print("False")
couples([1,3,4,0,2,5],2)
couples([3,2,0,1],0)
couples([1,0],0)
