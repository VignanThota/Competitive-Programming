def key_match(l):
	marked =[]
	for i in range(len(l)):
		marked.append('N')
	marked[0]='O'
	for i in range(len(l)):
		for j in range(len(l[i])):
			if(i==0 and marked[i]=='N' or marked[i]=='O' and l[i][j]<len(l)):
				marked[l[i][j]]='O'
	c = 0
	# print(marked)
	for i in range(len(marked)):
		if(marked[i] == 'N'):
			print("False")
			c = 0
			break
		else:
			c+=1
	if(c!=0):
		print("True")




key_match([[1], [0,2], [3]])
key_match([[1,3], [3,0,1], [2],[0]])
key_match([[1,2,3], [0], [0],[0]])
key_match([[1], [0,2,4], [1,3,4], [2], [1,2]])
key_match([[1], [2,3], [1,2], [4], [1], [5]])
key_match([[1], [2], [3], [4], [2]])
key_match([[1], [1,3], [2], [2,4,6], [], [1,2,3], [1]])
