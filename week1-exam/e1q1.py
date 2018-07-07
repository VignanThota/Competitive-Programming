def smatch(s1,t1):
	s = s1.replace(" ","").lower()
	t = t1.replace(" ","").lower()
	print()
	print(s1)
	print(t1)
	ds = {}
	dt = {}
	c = 0
	for i in range(len(s)):
		if s[i] not in ds:
			ds[s[i]] = 1
		else:
			ds[s[i]]+=1
	for i in range(len(t)):
		if t[i] not in dt:
			dt[t[i]] = 1
		else:
			dt[t[i]]+=1
	for i in dt:
		if i in ds:
			if dt[i]==ds[i]:
				c+=1
				continue
			else:
				c = 0
				print("False")
				break
		else:
				c = 0
				print("False")
				break

	if(c != 0):
		print("True")
smatch('anagram','nagaram')
smatch('keep', 'peek')
smatch('Mother In Law', 'Hitler Woman')
smatch('School Master', 'The Classroom')
smatch('ASTRONOMERS', 'NO MORE STARS')
smatch('Toss', 'Shot')
smatch('joy', 'enjoy')
smatch('Debit Card','Bad Credit')
smatch('SiLeNt CAT', 'LisTen AcT')
smatch('Dormitory', 'Dirty Room')
